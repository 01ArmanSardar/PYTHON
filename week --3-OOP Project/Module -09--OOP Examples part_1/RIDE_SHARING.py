from abc import ABC ,abstractmethod
from datetime import datetime
class Ride_sharing:
    def __init__(self,name,ceo):
        self.name=name
        self.ceo=ceo
        self.riders=[]
        self.drivers=[]
        self.rides=[]
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    def __repr__(self):
        return f'{self.name} with riders : {len(self.riders)} and drivers {len(self.drivers)}'
        
    
class User(ABC):
    def __init__(self,name,email,nid) :
        self.name=name
        self.email=email
        self.__id=0
        self.__nid=nid
        self.walet=0
        self.curent_ride=None
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email,nid,curent_location,initial_amount):
        self.walet=initial_amount
        self.curent_location=curent_location
        self.curent_ride=None
        super().__init__(name, email,nid)
    def display_profile(self):
        print(f'rider name  is{self.name} rider adress {self.email}')
    def update_location(self,curent_location):
        self.curent_location=curent_location
    def in_amount(self,amount):
        if amount>0:
            self.walet+=amount
    def update_location(self,curent_location):
        self.curent_location=curent_location
    def request_ride(self,ride_sharing,destanation):
        if not self.curent_ride:
            ride_request=Ride_Request(self,destanation)
            ride_matcher=Ride_Matching(ride_sharing.drivers)
            ride=ride_matcher.find_driver(ride_request)
            print('got the ride',ride)
            self.curent_ride=ride
    def show_current_ride(self):
        print(self.curent_ride)

class Driver(User):
    def __init__(self, name, email,nid,curent_location):
        super().__init__(name, email, nid)    
        self.curent_location=curent_location
        self.walet=0
    def display_profile(self):
        print(f'driver name is {self.name} & email is{self.email}')

    def accept_ride(self,ride):
        ride.set_driver(self)
class Ride:
    def __init__(self,start_location,end_location):
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimeted_fare=None
    def set_driver(self,driver):
        self.driver=driver
    def start_ride(self):
        self.start_time=datetime.now()
    def end_ride(self,rider,amount):
        self.end_time=datetime.now()
        self.rider.wallet -=self.estimeted_fare
        self.driver.wallet +=self.estimeted_fare
    def __repr__(self):
        return f'ride details .started:{self.start_location}, to {self.end_location}'
class Ride_Request:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location
class Ride_Matching:
    def __init__ (self,drivers):
        self.avilable_drivers=drivers
    def find_driver(self,ride_request):
        if len(self.avilable_drivers)>0:
            #TODO :find the closest driver of the rider
            driver=self.avilable_drivers[0]
            ride=Ride(ride_request.rider.curent_location,ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicale(ABC):
    speed={
    'car':50,
    'Bike':70,
    'cng':40
    }
    def __init__(self,vehicaly_type,license_plat,rate):
        self.vehicaly_type=vehicaly_type
        self.license_plat=license_plat
        self.rate=rate
        self.status='avilable'
    @abstractmethod
    def strat_drive(self):
        pass
class Car(Vehicale):
    def __init__(self, vehicaly_type, license_plat, rate):
        super().__init__(vehicaly_type, license_plat, rate)
    def start_drive(self):
        self.status='unabilable'
class bike(Vehicale):
    def __init__(self, vehicaly_type, license_plat, rate):
        super().__init__(vehicaly_type, license_plat, rate)
    
    def start_drive(self):
        self.status='busy'
joy_bangla_ride_sharing=Ride_sharing('joy_bangla','shekHasina')
Arman=Rider('arsa','arman@.com',5648,'mohakhali',1200)
joy_bangla_ride_sharing.add_rider('arman')
kala_pakhi=Driver('kala pakhi','kalasada@.com',1254,'gulshan 1')
joy_bangla_ride_sharing.add_driver(kala_pakhi)
print(joy_bangla_ride_sharing)
Arman.request_ride(joy_bangla_ride_sharing,'Uttara')
Arman.show_current_ride()