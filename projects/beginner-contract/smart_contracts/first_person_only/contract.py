from algopy import ARC4Contract, String, UInt64, GlobalState, Txn, Global
from algopy.arc4 import abimethod


class Counter(ARC4Contract):
    def __init__(self)->None:
        self.counter = GlobalState(UInt64(0))
    @abimethod()
    def call(self) -> String:
        assert self.counter.value ==0, "The method can only be called for once"
        self.counter.value = UInt64(1)
        return String("Method called succesfully!!")
    @abimethod()
    def reset(self) -> String:
        assert Txn.sender == Global.creator_address, "Only the creator can call this method"        
        self.counter.value = UInt64(0)
        return String("Counter reset succesfully!!")
