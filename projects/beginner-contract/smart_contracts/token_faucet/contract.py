from algopy import ARC4Contract, String, itxn, Txn, Global
from algopy.arc4 import abimethod


class Transfer(ARC4Contract):
    @abimethod()
    def fund(self) -> None:
        assert (Global.current_application_address.balance - Global.current_application_address.min_balance) > 1000000, "No money"
        itxn.Payment(
            receiver=Txn.sender,  # The sender is the receiver in this case
            sender= Global.current_application_address,
            amount=1000000,  # Amount in microAlgos
            note=String("Funding the receiver account"),
        ).submit()


