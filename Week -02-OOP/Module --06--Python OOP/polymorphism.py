# poly --> many (multiple)
#morph --> shape/different
# ai jeh program tah teh make_sound jeh method tah,amrah sei method tah keh,parent class chara child class a o kintu use kortechi ,abong ai make_sound method tah akek  class a akek implimantation korteche,akek class seh akek result dicceh,ai bisoy tai mulotoh polymorphism,,,manhe poly-manhe bohu,morphi-manhe vibinno, manhe aktah method er bohu abong vibhinno vabhe bebohar tah kei polymorphism bolah hoie takhe.
class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        print('animal make sound')
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('meow meow')
class dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('geow geow') 
class goat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_sound(self):
        print('beh beh')
kalu=Cat('KALU')
kalu.make_sound()
balu=dog('BALU')
balu.make_sound()
messi=goat('messs')
messi.make_sound()
lessi=goat('less')
lessi.make_sound()
print('\n')
animals=[kalu,balu,messi,lessi]
for animal in animals: # make_sound er kintu akhneo aktah use hocceh , moddah khotah aktah method er bohu abong bhivinno bebohar.
    animal.make_sound()
        