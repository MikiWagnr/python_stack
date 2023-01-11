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
    # def display_all_accounts(cls):
    #     for all_accounts in cls.all_accounts:
    #         print(f"{all_accounts.useracc} has : ${all_accounts.balance} and interest rate is {all_accounts.rate}%")

# user1= BankAccount('Jemma', 0.5, 600)
# user1.deposit(50).deposit(25).deposit(25).withdraw(150).yield_interest().display_account_info()

# user2 = BankAccount('Fitz', 0.1, 500)
# user2.deposit(10).deposit(10).withdraw(50).withdraw(25).withdraw(25).withdraw(50).display_account_info().yield_interest()

# useracc.display_all_accounts()

class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount,i):
        self.account[i].deposit(amount)
        return self

    def make_withdrawal(self, amount,i):
        self.account[i].withdraw(amount)
        return self

    def display_user_balance(self,i):
        self.account[i].display_account_info()
        print(f"Current balance: ${self.account[i].balance}")
        return self

    def transfer_money(self,amount,otheruser,i,j):
        self.account[i].withdraw(amount)
        otheruser.account[j].deposit(amount)
        self.account[i].display_account_info()
        otheruser.account[j].display_account_info()



useracc1 = User('Charles Xavier', 'TomemyXmen@Xintstitute.com',[BankAccount(int_rate = 0.02, balance = 0), BankAccount(int_rate = 0.1, balance = 1000)])
useracc1.make_deposit(500,0).make_withdrawal(50,0).display_user_balance(0)

useracc2 = User('Tony Stark', 'iamironman@starkindustries.com',[BankAccount(int_rate = 0.02, balance = 0), BankAccount(int_rate = 0.1, balance = 1000)])
useracc2.make_deposit(500,1).make_withdrawal(50,1).display_user_balance(1)

useracc1.transfer_money(200, useracc2, 0, 1)