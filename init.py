import datetime

# This dictiionary is a hash map store for all SACCO accounts
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
        self.deposits = LinkedList() # only deposits
        self.withdraws = LinkedList() # only withdraws
        self.transactions = LinkedList() # has both withdrawal and deposits
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

            # add deposit record
            self.deposits.append(depositInfo)

            # record this transaction
            self.transactions.append(depositInfo)

            print("Thanks for depositing..")
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
            
            # add withdraw record
            self.withdraws.append(withdrawInfo)

            # add transaction record
            self.transactions.append(withdrawInfo)

            print(f"Thanks, you've withdrawn.. UGX {amount}")
        else:
            print("Insufficient Account Balance")

    
    def get_account_balance(self):
        print(f"Your Balance is = UGX {self.balance}")

    def get_account_statement(self):
        print("---STATEMENT-START---")
        self.transactions.print_all_transactions()
        print("---END---")

    def get_last_withdraw(self):
        self.withdraws.print_last_transaction()

    def get_last_deposit(self):
        self.deposits.print_last_transaction()

# Linked List class (For withdraws & deposits)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_last_transaction(self):
        current = self.head
        if current is None:
            print("No withdraws/deposits found.")
        else:
            print(current.data)
            current = current.next

    def print_all_transactions(self):
        current = self.head
        if current is None:
            print("No withdraws/deposits found.")
        while current:
            print(current.data)
            current = current.next


# +++++++++++++++++++++++
# Interface for running app
# +++++++++++++++++++++++

running_state = True

while(running_state):
    # create SACCO Member Account
    member_status = input("\nDo you have a SACCO Account? Yes/No\n")

    if(member_status == "Yes"):

        # Authentication
        farmer_id = input("\nEnter your FarmerID\n")
        # check is the farmerID entered has an account setup
        farmer_account = farmer_account_auth(farmer_id)

        # Choose a Service
        service_req = input("\nChoose A Service\n 1. Deposit\n 2. Withdraw\n 3. Check Balance\n 4. Get full Statement\n 5. Get last withdraw made\n 6. Get last deposit made\n\n")
        
        # Context Switch based on what service choice
        match service_req:
            case '1':
                farmer_account.deposit_money()
            case '2':
                farmer_account.withdraw_money()
            case '3':
                farmer_account.get_account_balance()
            case '4':
                farmer_account.get_account_statement()
            case '5':
                farmer_account.get_last_withdraw()
            case '6':
                farmer_account.get_last_deposit()
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



