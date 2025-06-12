from algopy import arc4, Global, Txn, log

class SingleOwner(arc4.ARC4Contract):
    @arc4.abimethod()
    def check(self) -> None:
        assert Txn.sender == Global.creator_address
        log("Authorized call")

