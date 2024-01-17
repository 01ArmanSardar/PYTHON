from abc import ABC, abstractmethod
#abc = abstract base class.
class Animal(ABC):
    @abstractmethod
    def kushul_binimoi (self):
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
