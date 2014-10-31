
 
class Person():
    print("New customer.")

class Checking_Acct(Person):
    money = 0
    def __init__(self):
        print("Checking Account opened.")
        
    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        self.money -= amount

    def wire_transfer(self, amount):
        self.money -= amount
 
    def interest(self, m):   # APY, NYSE: BAC  
        if money < 10000:
            self.money *= (1+ 0.0001/m)**m
        elif money < 100000 and money >= 10000:
            self.money *= (1+ 0.0002/m)**m
        else:
            self.money *= (1+ 0.0003/m)**m
            
    def payments(self, money):
        self.money -= 5000

    def fee(self, amount):
        self.money -= ((1+0.00005/m)**m)*amount*(0.001)


class Savings_Acct(Person):
    savings_money = 0
    def __init__(self):
         print("Savings Account opened.")
         
    def savings_deposit(self, amount):
        self.savings_money += amount 

    def savings_interest(self, m):
        self.savings_money *= (1+ 0.0001/m)**m

    def savings_withdraw(self, amount):
        self.savings_withdraw -= amount 

money = 7000             # automatic deposit 
m = 12                   # m = months 
acct_transf = 500 

person = Checking_Acct()

second_account = Savings_Acct() 

for i in range(m):
    person.fee(money)
    person.deposit(money)
    person.interest(m)
    person.payments(money)
    person.withdraw(acct_transf)
    second_account.savings_deposit(acct_transf)
    second_account.savings_interest(m)
 

print("Checking Account Balance: %.2f" % person.money)
print("Savings Account Balance: %.2f" % second_account.savings_money)
 
 




