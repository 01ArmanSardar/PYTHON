from abc import ABC, abstractmethod # abc aktah built_in module jetah tekhe amrah Abstract Base Class import korlam.
#abc = abstract base class.
class Animal(ABC):#Abstract Base Class er stahe inherit korlam
    @abstractmethod#enforce all derived class to have a kusul_binimoi method.
    def kushul_binimoi (self):# ai method tar uporeh  @abstractmethod leklham ,manhe akhn Animal class er jotogulah derived class takbhe,shob derived class a ai method tah use koret hobhe
        print('hey ANIMAl, how are you')
    def move(self):
        pass
class Cat(Animal):
    def __init__(self,name) -> None:
        self.catagory='Cat'
        self.name=name
        super().__init__()
    def kushul_binimoi(self):
        print('hey cat ,how are you.')
ash=Cat('kalu')
ash.kushul_binimoi()
