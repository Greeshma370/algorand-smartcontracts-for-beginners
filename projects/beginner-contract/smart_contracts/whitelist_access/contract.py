from algopy import ARC4Contract,BoxMap, Txn, Global, urange
from algopy.arc4 import abimethod, Address, String, DynamicArray

class DynamicArrayContract(ARC4Contract):
    def __init__(self) -> None:
        self.A = BoxMap(String,DynamicArray[Address])

    @abimethod()
    def add(self,name: String, account: Address) -> None:
        assert Txn.sender == Global.creator_address, "Only the creator can add addresses"
        if name in self.A:
            exist= False
            for index in urange(self.A[name].length):
                if self.A[name][index] == account:
                    exist = True
                    break
            if not exist:
                self.A[name].append(account)
        else:
            # Create a new dynamic array if it does not exist
            self.A[name] = DynamicArray[Address](account)

    @abimethod()
    def check(self,name: String, account: Address) -> bool:
        if name in self.A:
            for index in urange(self.A[name].length):
                if self.A[name][index] == account:
                    return True
        return False
