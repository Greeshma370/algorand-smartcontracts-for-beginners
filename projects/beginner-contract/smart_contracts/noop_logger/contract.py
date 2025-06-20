from algopy import Contract, log

class NoopLogger(Contract):
    def approval_program(self) -> bool:
        log("hey there") 
        return True
    def clear_state_program(self) -> bool:
        return True
