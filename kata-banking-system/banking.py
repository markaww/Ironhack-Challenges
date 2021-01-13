
Class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        print('customer created')
        
# withdraw method
    
    def withdraw(self, withdraw_amt):
        self.withdraw_amt = withdraw_amt
        
        if self.withdraw_amt > self.balance:
            print('insufficient funds')
        elif self.withdraw_amt < self.balance:
            self.balance -= self.withdraw_amt
            print(f'{self.name} has {self.balance}.')
            
# check method
# Q: How do I stop the second loop (transaction occurs) if first loop self.other_checking_account == False?     
            
    def check(self, other_name, check_amt, other_balance, other_checking_account):
        self.other = other_name
        self.check_amt = check_amt
        self.other_balance = other_balance
        self.other_checking_account = other_checking_account
        
        if self.other_checking_account == True:  
            print('transaction processing')
            
        elif self.other_checking_account == False:
            print(f"{self.other} doesn't have a checking account")
            
        
        if self.other_balance > self.check_amt:
                self.balance += self.check_amt
                self.other_balance -= self.check_amt
                print(f'{self.name} has {self.balance}, {self.other} has {self.other_balance}.')
        elif self.other_balance < self.check_amt:
                print('insufficient funds')
        
# add method


    def add(self, add_amt):
        self.add_amt = add_amt
        self.balance += self.add_amt
        print(f'{self.name} has {self.balance}.')
        
