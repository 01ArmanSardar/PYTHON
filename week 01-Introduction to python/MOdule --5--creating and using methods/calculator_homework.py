class calculator:
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
cal.divide(20,2)