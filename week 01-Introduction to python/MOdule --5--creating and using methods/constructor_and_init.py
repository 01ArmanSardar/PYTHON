class Phone:
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

    def send_sms(self,phone,sms): #atah keh bolhe method
        text=f'phone number {phone} sms is {sms}'
        print(text)

myphone=Phone('arman','oppo',17000) #phone calss er moddeh amrah jeh def __init__  use koralm atah kind of c++ er constructor er moto kaj koreh,atah set koreh deor por jkhn e Phone class er kono aktah object banbho tkhn amrah def __init__ er moddeh jeh paramatter gulah takbhe seh gulu use koree difrrent diffrent object use korteh prabho.jmn a program a myphone ,herphone ,dadphone banaichi,
print(myphone.owner,myphone.brand,myphone.price)

herphone=Phone('minara','samsung',6700)
print(herphone.owner,herphone.brand,herphone.price)

dadphone=Phone('abbu','symphony',7000)
print(dadphone.owner,dadphone.brand,dadphone.price)

# pen homework

""" class pen:
    def __init__(self,owner,color,price):
        self.owner=owner
        self.color=color
        self.price=price
janntpen=pen('jannat','green',5)
print(janntpen.owner,janntpen.color,janntpen.price)
mypen=pen('arman','blue',10)
print(mypen.owner,mypen.color,mypen.price)
marjupen=pen('marjan','black',15)
print(marjupen.owner,marjupen.color,marjupen.price) """

        
