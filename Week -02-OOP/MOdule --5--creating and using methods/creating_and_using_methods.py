class phone:
    name='samsung'
    color=1200
    owner='microsoft'
    features=['camera','speaker','hammer']

    def call(self): #it's call method
        print('\ncalling it-self\n')
    def send_sms(self,phone_num,sms):
        print(f'sending message this:{phone_num} and mesage is :{sms}')
myphone=phone()# akhne python   myphone   jetah leklam atai kintu object,myphone er jaigi onno kichu o likteh pari,akhne phoen er khota hocceh toh tai myphone liklam ar kih
myphone.call()
myphone.send_sms(1859136957, 'i missed you')

# calculator homework

""" class calculator:
    brand='casio'
    def add (self,num1,num2):
        sum=num1+num2
        print (sum)
    def deduct(self,num1,num2):
        deducts=num1-num2
        print(deducts)
    def multiply(self,num1,num2):
        ghun=num1*num2
        print(ghun)
    def divide(self,num1,num2):
        vhag=num1//num2
        print(vhag)
cal=calculator()
cal.add(10,20)
cal.deduct(20,10)
cal.multiply(10,4)
cal.divide(20,2) """