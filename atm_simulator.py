#Simulate ATM withdrawal using while loops and conditions.
password = "exchange"
attempts = 3


while attempts != 0:
    user_pin = input("Input your pin: ")

    if user_pin == password:
        print("Access granted")
        break

    else:
        attempts -= 1
        print("Incorrect password. Attempts left: ", attempts)
    
    if attempts == 0:
        print("Too many attempts")
        break

account_balance = 50000
def withdrawal():
        if withdraw < account_balance:
            account_balance -= withdraw
            print(f"Here's your sum of ${withdraw}", end=" ")
            print(f"Balance remaining: ${account_balance}")
            print("Thank you for banking with us!")
        return account_balance


while user_pin == password:
    user_option = input("Would you like to withdraw ? (Y/N): ").capitalize()

    if user_option == "N":
        print("Thank you for banking with us.")
        break
    if user_option == "Y":
        withdraw = int(input("Enter amount to withdraw: "))

        if withdraw > account_balance:
            print("Insufficient funds!")

        elif withdraw <= 0:
            print("Invalid amount!")

        elif withdraw < account_balance:
            #account_balance -= withdraw
            #print(f"Here's your sum of ${withdraw}", end=" ")
            #print(f"Balance remaining: ${account_balance}")
            #print("Thank you for banking with us!")
            withdrawal()
            break

    else:
        print("Invalid option, please enter Y or N.")

    
        
        