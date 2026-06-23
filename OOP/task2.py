class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def Withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Bank fee charged: {fee}")

    def display(self):
        print("Account Number:", self.accountNumber)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)

user = BankAccount(1234,"sohail", 6000)
user.bankFees()
user.Deposit(500)
user.Withdrawal(4000)
user.display()