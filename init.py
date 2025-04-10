# import the account class module
from account import Account
from account_number_gen import SACCO_Member

# This dictiionary is a hash map store for all SACCO accounts
ac_numbers = {}

def farmer_account_auth(farmer_account_id):
    try:
        if isinstance(ac_numbers[farmer_account_id], Account):
            print("Account Exists")
        
        return ac_numbers[farmer_account_id]
    except:
        print("No account with given id - Create account.")
        return False


# +++++++++++++++++++++++
# Interface for running app
# +++++++++++++++++++++++

running_state = True
logged_in = False
farmer_account = None

while running_state:
    if not logged_in:
        # Ask if the user has an account
        member_status = input("\nDo you have a SACCO Account Number? Yes/No\n")

        if member_status.lower() == "yes":
            # Authenticate
            sacco_account_number = input("\nEnter your SACCO Account Number ID\n")
            farmer_account = farmer_account_auth(sacco_account_number)

            if farmer_account:
                logged_in = True
                print(f"\nWelcome back!")
            else:
                print("Invalid FarmerID. Please try again.")
        else:
            # Create account
            print("\n**Account Creation Process...")
            name = input("Enter your full name:\n")
            age = input("Enter your age:\n")
            occupation = input("Enter your occupation:\n")
            address = input("Enter your residential address:\n")
            contact = input("Enter your contact number:\n")
            account_pin = input("Set a 4-digit account PIN:\n")

            new_sacco_member = SACCO_Member(name, age, occupation, address, contact, account_pin)
            generated_account_number = new_sacco_member.account_number

            new_account = Account(generated_account_number)
            ac_numbers[generated_account_number] = new_account

            print("\nCongrats! Account Created Successfully.")
            print(f"SACCO Member: {name}\nAccount ID: {generated_account_number}")
            print("______________________\n")
            
            farmer_account = new_account
            logged_in = True

    # If logged in, allow access to services
    if logged_in and farmer_account:
        service_req = input(
            "\nChoose A Service:\n"
            " 1. Deposit\n"
            " 2. Withdraw\n"
            " 3. Check Balance\n"
            " 4. Get Full Statement\n"
            " 5. Get Last Withdrawal\n"
            " 6. Get Last Deposit\n"
            " 7. Logout\n"
        )

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
            case '7':
                logged_in = False
                farmer_account = None
                print("You have been logged out.")
            case _:
                print("Invalid Option.. Try again\n")

    # Exit option
    stop_check = input("Type 'Exit' to stop, or press Enter to continue:\n")
    if stop_check.lower() == "exit":
        running_state = False

