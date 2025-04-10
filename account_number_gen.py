import uuid

class SACCO_Member:
    def __init__(self, name, age, occupation, address, contact, account_pin):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.address = address
        self.contact = contact
        self.account_pin = account_pin
        self.account_number = self.generate_account_id()

    def generate_account_id(self):
        # Generate a unique account ID using UUID4
        # Shorten using array slicing to keep it at only 5 characters
        return f"ACC-{str(uuid.uuid4())[:5]}"

    def get_account_info(self):
        return f"SACCO Member: {self.name}, Account ID: {self.account_number}"

# Example usage:
# member = SACCO_Member(
#     name="Alice K",
#     age=34,
#     occupation="Farmer",
#     address="Kyenjojo",
#     contact="0700123456",
#     account_pin="4567"
# )

# print(member.get_account_info())