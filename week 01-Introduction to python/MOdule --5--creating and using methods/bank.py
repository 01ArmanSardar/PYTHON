""" class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    def witdraw(self,amount):
        if amount<self.min_withdraw:
            print('your withdraw amount is too mnimum')
        elif amount>self.max_withdraw:
            print('your withdraw amount is too much')          
        else:
            self.balance-=amount
            print (f'here is your money {amount}')
            print(f'your balnce after withdraw{self.balance}')
brac=Bank(15000)
brac.witdraw(100000000000)
brac.witdraw(2500)

dbbl=Bank(4000)
dbbl.deposit(1000)
dbbl.deposit(100)
print(f'dbbl balance after deposit {dbbl.get_balance()}') """

#homeWork
class exam:
    def __init__(self,sub):
        self.sub=sub
        self.minimum_marks_for_Aplus=70
        self.maximmum_marks_for_Aplus=100
    def attend_exam(self):
        print('thanks for attending')
    def get_marks(self,mymarks):
        if mymarks>self.minimum_marks_for_Aplus:
            print('you got a plus')

myexam=exam('vigghan')
myexam.get_marks(70)
myexam.attend_exam()
