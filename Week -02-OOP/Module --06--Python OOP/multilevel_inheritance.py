class vehicale:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __repr__(self) -> str:
        return f'{self.name} {self.price}'
    def move(self):
        pass
class Bus(vehicale):
    def __init__(self, name, price,seat):
        self.seat=seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        
        return super().__repr__()

class track(vehicale):
    def __init__(self, name, price,weight):
        self.weight=weight
        super().__init__(name, price)
class ACbus(Bus):
    def __init__(self, name, price, seat,tempareture):
        self.tempareture=tempareture
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        
        return super().__repr__()

green_line=ACbus('green',5000000,20,f'{16} celcius')
print(green_line)
        