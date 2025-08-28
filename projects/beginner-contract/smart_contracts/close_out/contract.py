from algopy import ARC4Contract, LocalState, UInt64, Txn
from algopy.arc4 import abimethod

class LoyaltyPoints(ARC4Contract):
    def __init__(self) -> None:
        # Each customer has their own loyalty points in local state
        self.points = LocalState(UInt64)

    @abimethod(allow_actions=["OptIn"])
    def opt_in(self) -> None:
        # Initialize points to zero when a customer joins
        self.points[Txn.sender] = UInt64(0)

    @abimethod
    def earn_points(self, amount: UInt64) -> UInt64:
        # Add points for the customer
        self.points[Txn.sender] += amount
        return self.points[Txn.sender]

    @abimethod(allow_actions=["CloseOut"])
    def closeout(self) -> None:
        # Reset points to zero when the customer leaves
        self.points[Txn.sender] = UInt64(0)

    def clear_state_program(self) -> bool:
        # Approve all clear state calls (emergency exit)
        return True
