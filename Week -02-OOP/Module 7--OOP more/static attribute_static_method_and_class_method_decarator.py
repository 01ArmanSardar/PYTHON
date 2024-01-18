#static attribute (also called class atrribute )
#static method using @staticmethod decorator
#class method using @classmethod dcortaor
class Shopping:
    cart=[]#class attribute /static attribute,ai attribute tah class er shobgulah instance er sate share hoi.
    origin='china' #this is also a static attribute

    def __init__(self,name,location):
        self.name='Eastren plaza' # this is instance attribute 
        self.location='banglamotor' 
    @classmethod # kono aktah method er upor ai @classmethod decorator tah use korleh sei method tah amrah direct class diei e use korteh parih
    def hudai_dekhi(self,item):
        print(f'hudai dekhi kintu kinmuh nah but akta {item} nie nara chara korih')
    @staticmethod # static method tah keh instance charai use korah jai, & static method tah keh class die oh shora shori use korah jai ,abong ai method er belai method argument er moddhe self tah diteh hoi nah.
    def multifly(a,b):
        print(a*b)

Shopping.hudai_dekhi('lunghi')
Shopping.multifly(6,9)