# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified

# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address
        self.account_balance = 0
    
    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f'User: {self.name}, Balance:${self.account_balance}')
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self



Tom = User('Tom Featherington', 'tfeatherington3@cmail.com')

Tom.make_deposit(250).make_deposit(100).make_deposit(75).make_withdrawal(95).display_user_balance()

Jerry = User('Jerry Tuscaloosa', 'jerryt@cmail.com')

Jerry.make_deposit(300).make_deposit(350).make_withdrawal(125).make_withdrawal(50).display_user_balance()

Violet = User('Violet Meriwhether', 'vmeriw@flowers.com')

Violet.make_deposit(500).make_withdrawal(125).make_withdrawal(50).make_withdrawal(150).display_user_balance()

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

Tom.transfer_money(Violet, 50).display_user_balance()
Violet.display_user_balance()