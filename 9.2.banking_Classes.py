class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(self.name, "has", self.balance)

acc1 = BankAccount("Fahad", 1000)

acc1.deposit(500)
acc1.show_balance()