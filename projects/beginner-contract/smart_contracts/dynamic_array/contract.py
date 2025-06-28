from algopy import ARC4Contract,BoxMap, Txn, Global, urange
from algopy.arc4 import abimethod, Address, String, DynamicArray

class DynamicArrayContract(ARC4Contract):
    def __init__(self) -> None:
        self.List = BoxMap(String,DynamicArray[String])


    @abimethod()
    def create(self,section: String) -> None:
        self.List[section] = DynamicArray[String]()
        

    @abimethod()
    def add(self,section: String, name: String) -> None:
        assert section in self.List, "dynamic array not created for this respective section"
        exist = False
        for index in urange(self.List[section].length):
            if self.List[section][index] == name:
                exist = True
                break
        if not exist:
            self.List[section].append(name)

    @abimethod()
    def check(self,section: String, name: String) -> bool:
        if section in self.List:
            for index in urange(self.List[section].length):
                if self.List[section][index] == name:
                    return True
        return False
    
    @abimethod()
    def get(self,section: String) -> DynamicArray[String]:
        assert section in self.List, "dynamic array not created for this respective section"
        return self.List[section]
    
    @abimethod()
    def delete(self,section: String, name: String) -> None: 
        assert section in self.List, "dynamic array not created for this respective section"
        new_section = DynamicArray[String]()
        # Iterate through the dynamic array and remove the specified name
        for index in urange(self.List[section].length):
            if self.List[section][index] != name:
                new_section.append(name)
                
        self.List[section] = new_section.copy()
        
    @abimethod()
    def delete_section(self,section: String) -> None:
        assert section in self.List, "dynamic array not created for this respective section"
        del self.List[section]
