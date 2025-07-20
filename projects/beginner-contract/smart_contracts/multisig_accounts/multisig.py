from algokit_utils import Account, SigningAccount, MultisigMetadata
from algokit_utils.algorand import AlgorandClient
from algokit_utils.models.amount import AlgoAmount
from algokit_utils.transactions.transaction_composer import (
    AssetCreateParams,
    AssetConfigParams,
    AssetOptInParams,
    AssetTransferParams,
)

# 1. Set up Algorand client (using LocalNet for testing)
algorand = AlgorandClient.default_localnet()

# 2. Create/fund sender and receiver accounts
account1 = algorand.account.random()
account2 = algorand.account.random()
account3 = algorand.account.random()
dispenser = algorand.account.localnet_dispenser()
algorand.account.ensure_funded(account1, dispenser, min_spending_balance=AlgoAmount.from_algo(10))
algorand.account.ensure_funded(account2, dispenser, min_spending_balance=AlgoAmount.from_algo(10))
algorand.account.ensure_funded(account3, dispenser, min_spending_balance=AlgoAmount.from_algo(10))


# Create a 2-of-3 multisig account
multisig_account = algorand.account.multisig(
    metadata=MultisigMetadata(
        version=1,
        threshold=2,
        addresses=[
            account1.address,
            account2.address,
            account3.address,
        ],
    ),
    signing_accounts=[account1, account2, account3],
)

print("Multisig Address:", multisig_account.address)

# Fund the multisig account with 10 Algos from the dispenser
algorand.account.ensure_funded(
    multisig_account.address, dispenser, AlgoAmount(algo=10)
)

asset_params = AssetCreateParams(
    sender=multisig_account.address,
    total=1_000_000,           # Total supply
    decimals=2,                # Number of decimals
    asset_name="MyToken",      # Full name
    unit_name="MTK",           # Unit/ticker
    manager=multisig_account.address,    # Set manager, reserve, freeze, clawback to sender
    reserve=multisig_account.address,
    freeze=multisig_account.address,
    clawback=multisig_account.address,
)
create_result = algorand.send.asset_create(asset_params)

# Perform a payment transaction from the multisig account
new_freeze_address = algorand.account.random().address
freeze_change_txn = algorand.send.asset_config(
    AssetConfigParams(        
        asset_id=create_result.asset_id,
        sender=multisig_account.address,
        signer=multisig_account.signer,
        manager=multisig_account.address,        
        clawback=multisig_account.address,
        freeze=new_freeze_address,
    )
)

print("\n✅ Transaction sent from multisig account for freeze change!")
print("TxID:", freeze_change_txn.tx_id)
