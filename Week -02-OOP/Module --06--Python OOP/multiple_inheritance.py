class Family:
    def __init__(self,address):
        self.address=address

class school:
    def __init__(self,id,level):
        self.id=id
        self.level=level
class sports:
    def __init__(self,game):
        self.game=game
class student(Family,school,sports): #vibhinnno class er tekeh attribute nie notun aktah class a setah add korah 
    def __init__(self, address,id,level,game):
        school.__init__(self,id,level)
        sports.__init__(self,game)
        Family.__init__(self,address)

        super().__init__(address)