from algopy import (Account, ARC4Contract, LocalState, UInt64, arc4 )


class LocalStorage(ARC4Contract):
    # example: INIT_LOCAL_STORAGE
    def __init__(self) -> None:
        ## Initialise local storages
        self.number = LocalState(UInt64)  # Uint64
    
    @arc4.abimethod()
    def set_value(self, account: Account, value: UInt64) -> None:
        """
        Initialize local storage for the given account.
        """
        self.number[account] = value
    @arc4.abimethod()
    def get_value(self, account: Account) -> UInt64:
        """
        Get the value from local storage for the given account.
        """
        return self.number[account]
    @arc4.abimethod()
    def clear_value(self, account: Account) -> None:
        """
        Clear the value from local storage for the given account.
        """
        del self.number[account]
