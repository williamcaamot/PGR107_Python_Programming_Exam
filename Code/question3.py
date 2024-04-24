class Message:
    def __init__(self, sender, recipient) -> None:
        self.addresses = (sender, recipient) # Tuple because I assume these will not change after instantiation
        self.recipient = recipient
        self.message = "" # Must be instance variable even though it's not set in the constructor (unique for all objectes created with Message class)

    def get_sender(self) -> str:
        return self.addresses[0]
    
    def get_recipient(self) -> str:
        return self.addresses[1]
    
    def append(self, message) -> None:
        self.message += message + "\n"

    def toString(self) -> str:
        return f"From: {self.sender} \nTo: {self.recipient} \n{self.message}"


# Executing code is in main.py