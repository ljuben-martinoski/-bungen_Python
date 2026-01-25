

"""

Build an ATM simulator with:
- Starting balance of $1000
- Menu with options:
  1. Check Balance
  2. Deposit
  3. Withdraw
  4. Exit
- Keep looping until user chooses Exit
- Don't allow withdrawals that exceed balance
- Use `continue` for invalid menu choice"""

def atm_machine():
    balance = 1000
    while True:
        print("\n ===ATM Menu===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3.Withdraw")
        print("4. Exit")
        choice = input()
        if choice == '1':
            print(f"Your curent Balance is : ${balance}")
        elif choice == '2':
            amount = float(input("Enter amopunt to deposit: $"))
            if amount > 0:
                balance += amount
                print(f"${amount} deposited successfully. ")
            else:
                print("Invalid amount .Please enter a positive number")
        elif choice == '3': # here is the withdraw option , and '3' is the choice for withdraw
            amount = float(input("Enter amount to Withdraw: $"))
            if amount > balance:
                print("Your dont have enough funds!! ")
            elif amount == balance:
                print("You will withdraw the whole Amount!!")
            elif amount < balance:
                balance -= amount
                print(f"Withdraw amount: ${amount}")
                print(f"Success! New balance: ${balance}")
            
        elif choice == '4':
            break
        
atm_machine()        