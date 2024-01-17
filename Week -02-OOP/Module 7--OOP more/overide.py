class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print('vat ,mach,goru,murgi')
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)

shakib=Cricketer('sakib',38,5,69,'bd')
shakib.eat()