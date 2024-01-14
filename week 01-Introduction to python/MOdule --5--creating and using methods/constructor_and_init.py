class Phone:
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

    def send_sms(self,phone,sms): #atah keh bolhe method
        text=f'phone number {phone} sms is {sms}'
        print(text)
myphone=Phone('arman','oppo',67000)
print(myphone.owner,myphone.brand,myphone.price)
herphone=Phone('sraboni','samsung',6700)
print(herphone.owner,herphone.brand,herphone.price)
dadphone=Phone('abbu','symphony',7000)
print(dadphone.owner,dadphone.brand,dadphone.price)
