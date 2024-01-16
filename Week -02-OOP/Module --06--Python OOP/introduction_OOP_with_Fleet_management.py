class Company:
    def __init__(self,name,address):
        self.name=name
        self.bus=[]
        self.drivers=[]
        self.routes=[]
        self.counter=[]
        self.manager=[]
        self.supervisors=[]

class Driver:
    def __init__(self,name,license,age):
        self.name=name
        self.license=license
        self.age=age

class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_tiket(self,start,destination):
        self.start=start
        self.destination=destination

class Passenger:
    pass     
        