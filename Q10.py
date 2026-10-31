class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully.")

    def check_balance(self):
        print("Account Balance:", self.__balance)


account = BankAccount(101, "Bhavya", 5000)

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid amount.")

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice.")