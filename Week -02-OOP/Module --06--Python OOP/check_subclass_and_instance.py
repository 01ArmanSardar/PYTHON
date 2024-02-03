class Book:
    def __init__(self,name):
        self.name=name
class Physics(Book):
    def __init__(self, name,lab):
        self.lab=lab
        super().__init__(name)
topon =Physics('topon',True)

print(isinstance(topon,Book))# topon kih Book er subinstance kintah setah check korlam
print(issubclass(Physics,Book)) #physics kih Book er subclass kinah setah check korlam
        