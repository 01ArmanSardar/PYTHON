# base class / parent class /common attribute + functionality class
class gadget: # niche laptop ,phone ,camera namer 3tah class aceh oi 3 tah class er common attribute kintu name, brand, price, color, abong aktah common method run , toh amrah sei common attribute gulah,abong run metohd tah keh ai class a nie aslam ,ar atakei normally inheritance bolah hoi
    def __init__(self,name,brand,price,color):
        self.name=name
        self.brand=brand
        self.price=price
        self.color=color
    def run (self):
        print(f'runnign phone is {self.brand}')    
# derived class / child class ,uncommon attribute +functionality class
class laptop:
    def __init__(self,name,brand,price,color,memory):   
        self.memory=memory
    def coding(self):
        return f'learning python and practicing'
class phone(gadget): #ai line tah teh jemon gadget class tah hocceh parent class ar phone class tah hocceh derived class,toh amrah parent class tekeh common attribute gulu nie derived class a use korte parbho,sudhu atrriut nah amra caileh common method parent class tekeh derived class a niteh parih
    def __init__(self,name,brand,price,color,dual_sim):
        self.dual_sim=dual_sim
        super().__init__(name,brand,price,color)
    
    def __repr__(self):
        return f'phone :{self.name} {self.brand} {self.price} {self.color} {self.dual_sim}'
        
    def calling_someone(self,number,sms):
        print(f'calling {number}for this message{sms}')

class camera:
    def __init__(self,name,brand,price,color,pixel):
        self.pixel=pixel
    def change_lens(self):
        pass

aru_phone=phone('samsung','SAMSUNG',12393,'blue','robi,airtel')
print(aru_phone)
print(aru_phone.name)
print(aru_phone)
