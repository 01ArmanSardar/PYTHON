# encapsulations --> hide details,encapsulations er bleai normally private attribute er use hoie takhe.
# acces modifier --> public ,protected,private
class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name # public attribute : kono aktah attribute normaly declare korle setah bydefult public attribute hobhe,manhe progrma er jeh kono jaigah tekeh setah acces kora jabhe
        self.__balance=initial_deposit # private attribute : kono aktah attribute for example  self.__balance, akhne 2 tah underscore die suru korlm taile ai balance tah sudhu class er moddei acces kora jabhe, manhe atah private
        # protected attribute : aktah underscore takleh setah keh protected attribute bolah hoie takhe.
    def deposit(self,amount): 
        self.__balance+=amount# ai line tah tei amra akpokar encapsulation kortechi,manhe amrah balance er sateh jeh deposti amount tah add koretchi setah class er bahire kauke dekacchi nah
    def get_balance(self):
        return self.__balance
rufsun=Bank('chotto bro',10000)
print(rufsun.holder_name)
rufsun.deposit(40000)
print(rufsun.get_balance())
#................ below line show how to try acces private attribute in class er bahireh
# print(dir(rufsun))
print(rufsun._Bank__balance)


        