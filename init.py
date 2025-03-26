import datetime

ac_numbers = {}

def farmer_account_auth(farmer_id):
    try:
        if isinstance(ac_numbers[farmer_id], Account):
            print("Account Exists")
        
        return ac_numbers[farmer_id]
    except:
        return "No account with given id - Create account."
    

class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.authCheck = False
        self.deposits = []
        self.transactions = [] # has both withdrawal and deposits
        self.created_at = datetime.datetime.now()

    # Create a DS for the deposits to ensure efficient insertion & retrieval
    # Use a Hash Map - for quick lookup of farmer's deposit history
    # Maintain and ordered list of deposits (use stack)
    def deposit_money(self):
        amount = input("Enter Deposit Amount\n")

        if int(amount) > 0:
            depositInfo = {
                "farmer_id": self.id,
                "amount": amount,
                "timeStamp": datetime.datetime.now(),
                "transaction_type": "Deposit"
            }
        
            self.balance += int(amount)

            self.deposits.insert(0, depositInfo)
            self.transactions.insert(0, depositInfo)
        else: 
            print("Deposit should be greater than zero")
        

    # Check amount before withdraw
    # Store & update farmer balances in constant time O(1)
    # Retrieving the most recent transcations first (Use Stack)
    # Store transaction with farmerID, Amount & Timestamp.
    def withdraw_money(self):
        # How much do you want to withdraw
        amount = input("Enter Withdraw Amount\n")
        # check if ammount is available
        if int(amount) <= self.balance:
            print("Withdrawing...")

            withdrawInfo = {
                "farmer_id": self.id,
                "amount": amount,
                "timeStamp": datetime.datetime.now(),
                "transaction_type": "Withdraw"
            }

            self.balance -= int(amount)
            self.transactions.insert(0, withdrawInfo)

        else:
            print("Insufficient Account Balance")

    
    def get_account_balance(self):
        print(f"Your Balance is = {self.balance}")

    def get_account_statement(self):
        print("---STATEMENT-START---")
        for transaction in self.transactions:
            print(f"{transaction}\n")
        print("---END---")

# Instances

# +++++++++++++++++++++++
# Interface for running app
# +++++++++++++++++++++++

running_state = True

while(running_state):
    # create SACCO Member
    member_status = input("\nDo you have a SACCO Account? Yes/No\n")

    if(member_status == "Yes"):

        # Authentication
        farmer_id = input("\nEnter your FarmerID\n")
        # check is the farmerID entered has an account setup
        farmer_account = farmer_account_auth(farmer_id)

        # Choose a Service
        service_req = input("\nChoose Service\n 1. Deposit\n 2. Withdraw\n 3. Check Balance\n 4. Get Statement\n")
        
        match service_req:
            case '1':
                farmer_account.deposit_money()
            case '2':
                farmer_account.withdraw_money()
            case '3':
                farmer_account.get_account_balance()
            case '4':
                farmer_account.get_account_statement()
            case _:
                print("Invalid Option.. Try again\n")

    else:
        print("\n**Account Creation Process...")
        farmer_id = input("Enter your given SACCO/FarmerID\n")

        # Check if the account already exists
        auth_response = farmer_account_auth(farmer_id)

        if isinstance(auth_response, Account):
            print("You have an account already...")
        else:
            new_account = Account(farmer_id)
            ac_numbers[farmer_id] = new_account

            print("\nCongs.. Account Created. \nUse FarmerId to access account")
            print("______________________\n")

        

       
    
    stop_check = input("Continue or Exit?\n")
    if(stop_check == "Exit"):
        running_state = False
    


# INGORE CODE BELOW



# SACCO Member class
# class SACCO_Member:
#     def __init__(self, name, farmer_id, age, occupation, address, contact, next_of_kin):
#         self.name = name
#         self.farmer_id = farmer_id
#         self.age = age
#         self.occupation = occupation
#         self.address = address
#         self.contact = contact
#         self.next_of_kin = next_of_kin



