class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money
arsa=User('aru',23,1000000)
print(arsa.__money)        