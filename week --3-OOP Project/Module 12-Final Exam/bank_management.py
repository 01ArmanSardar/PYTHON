class Bank:
    def __init__(self) -> None:
        self.total_balance=0
        self.total_loan=0
        self.loan_status=True
        self.account_list=[]
        self.bankrupt=False
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
    def total_loans(self):
        print(self.total_loan)
    def loan_status_(self,tru_fls):
        self.loan_status=tru_fls


class Account(Bank):
    # accounts=[]
    def __init__(self,name,Email,address,type):
        self.name=name
        self.Email = Email
        self.accountNo=name+Email
        self.address=address
        self.balance = 0
        self.type=type
        self.transction_history=[]
        self.loan_limit=2
        # Account.accounts.append(self)

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"\n--> Deposited {amount}. New balance: ${self.balance}")
            self.transction_history.append(amount)
        else:
            print("\n--> Invalid deposit amount")

    def withdraw(self, amount):
        
        if self.bankrupt==False:
            if amount >= 0 and amount <= self.balance:
                self.balance -= amount
                print(f"\nWithdrew ${amount}. New balance: ${self.balance}")
                self.transction_history.append(amount)
            else:
                print("\n withdrawal amount exceeded")
        else:
            print('your Bank is bankrupt')
        
            
    def check_avilable_balance(self):
        print(self.balance)

    def tranesfer_money(self,another_accNo,amount):
        #TODO cehck bank is bankrupt ?
        if self.bankrupt==False:
            if amount <=self.balance:
                self.balance-=amount
                another_accNo.balance+=amount
            else:
                print('Account does not exist')
        else:
            print('your Bank is bankrupt')
        

    def check_transction_history(self):
        for transct in self.transction_history:
            print(transct)
    def take_loan(self,amount):
        if self.loan_status==True:
            if self.loan_limit>0:
                self.balance+=amount
                self.loan_limit-=1
                self.total_loan+=amount
            else:
                 print('your loan limit exceeded')
        else:
            print('loan status is off')
    

class SavingsAccount(Account,Bank):
    def __init__(self,name,Email,address,):
        super().__init__(name,Email,address,"savings")
        self.accountNo=name+Email

   
class CurrentAccount(Account,Bank):
    def __init__(self,name,Email,address):
        super().__init__(name,Email,address,"current")
        self.accountNo=name+Email


    """ def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= -self.limit:
            self.balance -= amount
            print(f"\n--> Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("\n--> Invalid withdrawal amount or overdraft limit reached") """
            
   
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
        
        if currentUser.name!="Admin":
            
            print("1. check Balance")
            print("2. check transaction history")
            print("3. take loan")
            print("4. transfer money another user account")
            print('5 .deposit in account')
            print('6. withdraw the amount')
            print("7. Logout\n")
            
            op=int(input("Chhose Option:"))
            
            if op==1:
                amount=("Check Avilable balance :")
                currentUser.check_avilable_balance()
                
            elif op==2:
                currentUser.check_transction_history()
            
            elif op==3:
                amount=int(input('type loan ammount'))
                currentUser.take_loan(amount)
            
            elif op==4:
                anthr_acc_no=input('type account no')
                amount=int(input('type ammount'))
                currentUser.tranesfer_money(anthr_acc_no,amount)
            elif op==5:
                amount=int(input('type deposit ammount'))
                currentUser.deposit(amount)
            elif op==6:
                amount=int(input('type withdrwal ammount'))
                currentUser.withdraw(amount)
            elif op==7:
                currentUser=None
            else:
                print("Invalid Option")
        
        elif currentUser.name=='Admin':
            print("1. create an account")
            print("2. delete a account")
            print("3. all user account list")
            print("4. total avilable balance of the bank")
            print("5. cehck total loan ammount")
            print('6. on off the loan feature ')
            print('7.logout\n')
            
            
            op=int(input("Chhose Option:"))
            
            #op==1 incomplete
            if op==1:
                amount=int(input("Enter withdraw amount:"))
                currentUser.withdraw(amount)
                
            elif op==2:
                delete_account_no=input("enter deletable account no:")
                currentUser.delete_account(delete_account_no)
            
            elif op==3:
                currentUser.show_all_user_acount()
            
            elif op==4:
                print ('total avilable balance')
                currentUser.total_balances()
            elif op==5:
                print('total loan ammount')
                currentUser.total_loans()
            elif op==6:
                tru_flss=bool(input('type True or Flase for loan status'))
                currentUser.loan_status_(tru_flss)

            elif op==7:
                currentUser=None
            
            else:
                print("Invalid Option")