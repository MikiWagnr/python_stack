class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, name, int_rate, balance): 
        self.rate = int_rate
        self.balance = balance
        self.user = name
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('insufficient funds: charging a $5 fee.')
            self.balance -= 5
        return self

    def display_account_info(self):
        # your code here
        print('Account Balance:', self.balance)
        return self

    def yield_interest(self):
        # your code here
        if self.balance > 0:
            self.balance += self.balance * self.rate
        else:
            print('insufficient funds')
        return self

    @classmethod
    def display_all_acounts(cls):
        for all_accounts in cls.all_accounts:
            print(f"{all_accounts.user} has : ${all_accounts.balance} and interest rate is {all_accounts.rate}%")

useracc1 = BankAccount('Charles Xavier', .5, 100)
useracc1.deposit(50).deposit(25).deposit(25).withdraw(150).yield_interest().display_account_info()

useracc2 = BankAccount('Tony Stark', .5, 100)
useracc2.deposit(10).deposit(10).withdraw(50).withdraw(25).withdraw(25).withdraw(50).display_account_info().yield_interest()

BankAccount.display_all_acounts()