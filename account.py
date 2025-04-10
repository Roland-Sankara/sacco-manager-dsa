# import the linkedList class module
from linked_list import Node, LinkedList
# date&time module
import datetime

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
