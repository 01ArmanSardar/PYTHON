class Person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print('vat ,mach,goru,murgi')
    def exercise(self):
        raise NotImplementedError # atah manhe halka koreh bujai jeh,child class keh force kortechi ai method tah override korar jonno
    
class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team=team
        super().__init__(name, age, height, weight)
    # below method is overriding method,manhe ai method tah kintu parent class a impliment korah aceh,kintu trpr abr amra current class a eshe method tah teh abr onno kichu impliment korlam,ar atai normally overriding.
    def eat(self):
        print('vegitables')
    def exercise(self):
        print('gym a jai khai dhai')
    # + sign operator overload
    def __add__(self,other):
        return self.age+other.age
    # * sign operator overload
    def __mul__(self,other):
        return self.height*other.weight


shakib=Cricketer('sakib',38,5,69,'bd')
mushi=Cricketer('mushi',36,6,70,'bd')
# shakib.eat()
# shakib.exercise()

print(45+45)
print('shakib'+'rakib')
print([12,98]+[5,6,7,9,34])
print(shakib+mushi)# normally amrah shakib=mushi korle error asbhe,tobhe amrah jodhi shakib,mushi er jeh Cricketer class tah aceh setah teh jodhi aktah built-in method __add__ impliment kori tahole sei add method shakib mushi er age/height/weight etc jogh koreh diteh parbhe
print(shakib*mushi)# akhne jemon shakib er height er satteh mushi er weight ghun korlam ,ar jonno __mul__ name er aktah built in method use korlam
""" explanation of operator overloading :
uporer print(shakib + mushi) normally run korle error asbhe,tobhe amarh jodhi operator overloading kori manhe, akhne  +  jeh operator tah aceh setah keh aktah built in method  __add__  die implimanet krih tahole cailei amrah shakib mushi er age/weight/height etc jogh korteh parih,tobhe ai __add__ method tah sei class er moddeh implimnt krte hbhe given object gulu jei class er sei class a
 
 """