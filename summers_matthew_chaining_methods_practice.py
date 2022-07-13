class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User:", self.name + ", Balance:", self.account_balance)
        return self
    def transfer_money(self, amount, recipient):
        self.account_balance -= amount
        recipient.account_balance += amount
        print("User:", self.name + ", Balance:", self.account_balance)
        print("User:", recipient.name + ", Balance:", recipient.account_balance)
        return self

#Create 3 instances of User class
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
david = User("King David", "david@psalms.com")

#First User's actions
guido.make_deposit(501).make_deposit(500).make_deposit(500).make_withdrawal(1).display_user_balance()

#Second User's actions
monty.make_deposit(100).make_deposit(100).make_withdrawal(100).make_withdrawal(99).display_user_balance()

#Third User's actions
david.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

#BONUS - Transfer Money
guido.transfer_money(500, david)