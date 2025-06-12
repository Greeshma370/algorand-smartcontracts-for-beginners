from algopy import ARC4Contract, Account, String, Txn, UInt64, urange, ensure_budget, OpUpFeeSource, GlobalState
from algopy.arc4 import abimethod,Address
from algopy.op import sqrt


class Counter(ARC4Contract):
    def __init__(self)->None:
        self.counter = GlobalState(UInt64(0))
        self.last_changed_by = GlobalState(Address())

    @abimethod()
    def get_address(self)->Address:
        return self.last_changed_by.value
    
    @abimethod()
    def get(self)->UInt64:
        return self.counter.value
    
    @abimethod()
    def increment(self)->None:
        self.counter.value += UInt64(1)
        self.last_changed_by.value = Address(Txn.sender)
        
    @abimethod()
    def decrement(self)->None:
        if self.counter.value!=0:
            self.counter.value -= UInt64(1)
            self.last_changed_by.value = Address(Txn.sender)
        