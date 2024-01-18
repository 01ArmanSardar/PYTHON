class Shopping:
    cart=[]#class attribute /static attribute,ai attribute tah class er shobgulah instance er sate share hoi.
    origin='china' #this is also a static attribute

    def __init__(self,name,location):
        self.name='Eastren plaza' # this is instance attribute 
        self.location='banglamotor' 
    @classmethod # kono aktah method er upor ai @classmethod decorator tah use korleh sei method tah amrah direct class diei e use korteh parih
    def hudai_dekhi(self,item):
        print(f'hudai dekhi kintu kinmuh nah but akta {item} nie nara chara korih')

Shopping.hudai_dekhi('lunghi')
Bashundara=Shopping('bashundara','panthpath')
Bashundara.hudai_dekhi('lunghi')