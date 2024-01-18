# compositon & inheritance er moddeh defrence tah holoh ,inheritance  er belai berived class parent class er shobgulu common attribute nei ,ar composition sudhu selected attribute bah method nei,daranoa kichu tah arkm e
# for examole amrah vehicale er inheritance dekhi tahole ,
#bus is a vechical
# truck is a vehicale
# acbus is a vehicale
# but amrah jodhi niceh compostion er example dekhi
# Car has a engine
# Car has a Driver
""" class Engine:
    def __init__(self):
        pass
    def start(self):
        return 'engine started'
class Driver:
    def __init__(self) -> None:
        pass

class Car:
    def __init__(self) -> None:
        self.engine=Engine()
        self.driver=Driver()
    def start(self):
        self.engine.start()
pajero=Car()
pajero.start() """
#conputer has a cpu
#computer has a ram
# computer has a hard_drive
class CPU:
    def __init__(self,cores) -> None:
        self.cores=cores
class RAM:
    def __init__(self,size) -> None:
        self.size=size
class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity=capacity

class Computer:
    def __init__(self,cores,ram_size,hrdsk_capacity) -> None:
        self.cpu=CPU(cores)
        self.ram=RAM(ram_size)
        self.hrdsk_capacity=HardDrive(hrdsk_capacity)