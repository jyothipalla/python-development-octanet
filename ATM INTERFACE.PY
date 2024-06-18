class ATM:
    def __init__(self):
        self.user_id = None
        self.pin = None
        self.balance = 0
        self.transactions = []

    def start(self):
        self.user_id = input("Enter User ID: ")
        self.pin = input("Enter PIN: ")
        if self.authenticate_user():
            self.atm_operations()

    def authenticate_user(self):
        # Add your user authentication logic here
        # For simplicity, let's assume authentication is successful
        return True

    def atm_operations(self):
        while True:
            print("\nATM Operations:")
            print("1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.show_transactions()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.transfer()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def show_transactions(self):
        print("\nTransactions History:")
        for transaction in self.transactions:
            print(transaction)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: ${amount}")
            print(f"Withdrawn: ${amount}")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")
        print(f"Deposited: ${amount}")

    def transfer(self):
        amount = float(input("Enter the amount to transfer: "))
        recipient = input("Enter recipient's account number: ")
        # Add transfer logic here

# Main program
if __name__ == "__main__":
    atm = ATM()
    atm.start()
