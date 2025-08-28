from algopy import ARC4Contract, LocalState, UInt64, Txn
from algopy.arc4 import abimethod

class MyCounter(ARC4Contract):
    def __init__(self) -> None:
        # Define a local state variable for the counter
        self.my_counter = LocalState(UInt64)

    """
    Initialize the counter when an account opts in
    """
    @abimethod(allow_actions=["OptIn"])
    def opt_in(self) -> None:
        self.my_counter[Txn.sender] = UInt64(0)
