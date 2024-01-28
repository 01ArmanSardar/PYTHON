from abc import ABC, abstractmethod

class Bank:
    def __init__(self) -> None:
        self.total_balance=0
        self.total_loan=0
        self.loan_status=True
        self.account_list=[]
    def create_account(self,account):
        self.account_list.append(account)

    def delete_account(self,accountNo):
        self.account_list.remove(accountNo)
    
    def show_all_user_acount(self):
        for account in self.account_list:
            print(f'{account} \n')
    
    def total_balances(self):
        for account in self.account_list:
            self.total_balance+=account.balance


class Account(ABC):
    # accounts=[]
    def __init__(self,name,Email,address,type):
        self.name=name
        self.Email = Email
        self.accountNo=name+Email
        self.address=address
        self.balance = 0
        self.type=type
        # Account.accounts.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        #TODO cehck bank is bankrupt ?
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n withdrawal amount exceeded")
        
            
    def check_avilable_balance(self):
        print(self.balance)

    def tranesfer_money(self,another_accNo,amount):
        #TODO cehck bank is bankrupt ?
        if amount <=self.balance:
            self.balance-=amount
            another_accNo.balance+=amount
        else:
            print('Account does not exist')
        

    def check_transction_history(self):
        pass
    def take_loan(self):
        pass
    

class SavingsAccount(Account):
    def __init__(self,name,Email,address,):
        super().__init__(name,Email,address,"savings")
        self.accountNo=name+Email


class CurrentAccount(Account):
    def __init__(self,name,Email,address):
        super().__init__(name,Email,address,"current")
        self.accountNo=name+Email


    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached")
            
   
# Main program

currentUser=None

while(True):
    if currentUser==None:
        print("\n--> No user logged in !")
        ch=input("\n--> Register/Login (R/L) : ")
        if ch=="R":
            name=input("Name:")
            email=input("Email:")
            addrs=input("address:")
            a=input("Savings Account or Current Account (svA/cuA) :")
            if a=="sv":
                currentUser=SavingsAccount(name,email,addrs,)
            else:
                currentUser=CurrentAccount(name,email,addrs)
        else:
            no=input("Account Number:")
            for account in Account.accounts:
                
                if account.accountNo==no:
                    currentUser=account
                    break
                
    else:
        print(f"\nWelcome {currentUser.name} !\n")
        
        if currentUser.type=="savings":
            
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Apply Interset")
            print("6. Logout\n")
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                print("Homework")
            
            elif op==5:
                currentUser.apply_interest()
            
            elif op==6:
                currentUser=None
            else:
                print("Invalid Option")
        
        else:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Show Info")
            print("4. change Info")
            print("5. Logout\n")
            
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                amount=int(input("Enter deposit amount:"))
                currentUser.deposit(amount)
            
            elif op==3:
                currentUser.showInfo()
            
            elif op==4:
                print("Homework")
            
            elif op==5:
                currentUser=None
            
            else:
                print("Invalid Option")