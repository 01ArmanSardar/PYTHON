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