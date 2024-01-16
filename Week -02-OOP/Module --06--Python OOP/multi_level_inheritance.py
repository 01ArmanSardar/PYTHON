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
class phone:
    def __init__(self,name,brand,price,color,dual_sim):
        self.dual_sim=dual_sim
    def calling_someone(self,number,sms):
        print(f'calling {number}for this message{sms}')

class camera:
    def __init__(self,name,brand,price,color,pixel):
        self.pixel=pixel
    def change_lens(self):
        pass

aru_phone=phone(True)
aru_phone.calling_someone(9089,'valo achi')