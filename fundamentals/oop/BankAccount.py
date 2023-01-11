class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.rate = int_rate
        self.balance = balance
        # self.user = name
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('insufficient funds: charging a $5 fee.')
            self.balance -= 5
        return self

    def display_account_info(self):
        print('Account Balance:', self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.rate
        else:
            print('insufficient funds')
        return self

    # @classmethod
    # def display_all_acounts(cls):
    #     for all_accounts in cls.all_accounts:
    #         print(f"{all_accounts.user} has : ${all_accounts.balance} and interest rate is {all_accounts.rate}%")

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        print(f"Current balance: ${self.account.balance}")
        return self



useracc1 = User('Charles Xavier', 'TomemyXmen@Xintstitute.com')
useracc1.make_deposit(100).make_withdrawal(50).display_user_balance()
# useracc1.deposit(50).deposit(25).deposit(25).withdraw(150).yield_interest().display_account_info()

# useracc2 = BankAccount('Tony Stark', 'iamironman@starkindustries.com')
# useracc2.deposit(10).deposit(10).withdraw(50).withdraw(25).withdraw(25).withdraw(50).display_account_info().yield_interest()

# User.display_all_acounts()