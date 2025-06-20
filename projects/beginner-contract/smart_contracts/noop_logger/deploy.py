import algosdk
import base64

algodClient = algosdk.v2client.algod.AlgodClient(
    algod_token="a"*64,  # replace with your algod token
    algod_address="http://localhost:4001",
)

creator_private_key = algosdk.mnemonic.to_private_key("hope oblige salmon police cool useless under draw soda umbrella charge duty thought evoke spatial spend paddle squirrel roof dumb bridge assist lobster absorb kingdom")
creator_address = algosdk.account.address_from_private_key(creator_private_key)

local_schema = algosdk.transaction.StateSchema(num_uints=1, num_byte_slices=1)
global_schema = algosdk.transaction.StateSchema(num_uints=1, num_byte_slices=1)
# example: APP_SCHEMA

# example: APP_SOURCE
# read the `.teal` source files from disk
with open("../artifacts/noop_logger/NoopLogger.approval.teal", "r") as f:
    approval_program = f.read()

with open("../artifacts/noop_logger/NoopLogger.clear.teal", "r") as f:
    clear_program = f.read()

approval_result = algodClient.compile(approval_program)
approval_binary = base64.b64decode(approval_result["result"])

clear_result = algodClient.compile(clear_program)
clear_binary = base64.b64decode(clear_result["result"])

sp = algodClient.suggested_params()
# create the app create transaction, passing compiled programs and schema
app_create_txn = algosdk.transaction.ApplicationCreateTxn(
    creator_address,
    sp,
    algosdk.transaction.OnComplete.NoOpOC,
    approval_program=approval_binary,
    clear_program=clear_binary,
    global_schema=global_schema,
    local_schema=local_schema,
)
# sign transaction
signed_create_txn = app_create_txn.sign(creator_private_key)
txid = algodClient.send_transaction(signed_create_txn)
result = algosdk.transaction.wait_for_confirmation(algodClient, txid, 4)
app_id = result["application-index"]
print(f"Created app with id: {app_id}")



