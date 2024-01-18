# read only --> you can not set the value,value can not be changed.
#getter --> get a value of a property through a method,most of the time ,you will get the value of a private attribute.
#setter --> set a value of a property through a method ,most of the time you will set the value of a private property.
class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
    #Getter : below @property decorator is a getter without any setter is readonly attribute
    @property #kono aktah method keh jodhi property/attribute hisebhe use korteh chai tahole seh method er uporeh  @property  ai decorator tah use korteh hobhe
    def age(self):
        return self._age
    #Getter : below @property decorator is a getter without any setter is readonly attribute
    @property
    def salary(self):
        return self.__money
    
    #setter
    #setter korteh holleh obossoii setar getter takteh hobhe.
    @salary.setter
    def salary(self,value):
        if value<0:
            return 'salary can not be negative'
        self.__money+=value
arsa=User('aru',23,1000000)
# print(arsa.__money)  
# print(arsa.age())  
# print(arsa.age)  
# print(arsa.salary)
print(arsa.salary)
arsa.salary=4500
print(arsa.salary)
