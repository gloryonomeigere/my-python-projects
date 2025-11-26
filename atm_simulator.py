#Simulate ATM withdrawal using while loops and conditions.
password = "exchange"
attempts = 3
account_balance = 50000


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


while True:
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
            account_balance -= withdraw
            print("Here's your sum of $", withdraw)
            print("Balance remaining: ", account_balance)
            break
        
        