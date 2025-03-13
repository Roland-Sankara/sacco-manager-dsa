import datetime

ac_numbers = ['jk25', 'jdf26']

# SACCO Member class
class SACCO_Member:
    def __init__(self, name, farmer_id, age, occupation, address, contact, next_of_kin):
        self.name = name
        self.farmer_id = farmer_id
        self.age = age
        self.occupation = occupation
        self.address = address
        self.contact = contact
        self.next_of_kin = next_of_kin

class Account:
    def __init__(self, id):
        self.id = id
        self.balance = 0
        self.authCheck = False

    def farmer_id_auth(self):
        farmer_id_acounts = input("Enter Farmer ID\n")
        
        for ac in ac_numbers:
            if(farmer_id_acounts == ac):
                print("Auth Success")
                self.authCheck = True
                break
            else:
                print("Auth Fail")
                self.authCheck = False
        
        
    def deposit_money(self):
        if(self.authCheck):
            amount = input("Enter Amount\n")
            time_stamp = datetime.datetime.now()
            print({
                "amount": amount,
                "timeStamp": time_stamp
            })

            self.balance += int(amount)
        else:
            print("Invalid Account Number")


# Instances
# farmerOne = SACCO_Member("Roland", "22343JK", 20, "Engineer", "Kampala",)
# newAccount = Account("JK25")
# print(newAccount.id)
# newAccount.deposit_money()

# yoAccount = Account("JFD26")
# yoAccount.deposit_money()

# print(f"New's Account Balance = {newAccount.balance}")
# print(f"Yo's Account Balance = {yoAccount.balance}")

# if isinstance(yoAccount, Account):
#     print("Yes")
# else:
#     print("Not an instance")

testAccount = Account("JFD26")

testAccount.farmer_id_auth()
testAccount.deposit_money()



