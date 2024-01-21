# 1. float kivabeh kaj koreh
""" floattt=input('give me float value : ')
floatvalue=float(floattt)
print(type(floatvalue)) """
# 2. take 3 number from the user and give me the largest number
""" print('give me 3 number : ')
val1=input('input1 : ')
val2=input('input2 : ')
val3=input('input3 : ')
intval1=int(val1)
intval2=int(val2)
intval3=int(val3)
if intval1>=intval2 and intval1>=intval3:
    print(intval1)
elif intval2>=intval1 and intval2>=intval3:
    print(intval2)
else:
    print(intval3) """
# 3. take 3 numbers from the user and give me the sum of the numbers
""" print('give me 3 number : ')
val1=input('input1 : ')
val2=input('input2 : ')
val3=input('input3 : ')
intval1=int(val1)
intval2=int(val2)
intval3=int(val3)
print(intval1+intval2+intval3) """
# 4. run a loop and show  me the odd numbers between 39 to 68
""" num=39
while num<=68:
    num+=1
    if num%2==0:
        continue
    print(num) """
# 5. grade calculator in python
""" num=input('marks :')
intnum=int(num)
if intnum<=33:
    print('F  you are fail ,try next time')
elif intnum<=60:
    print('A-   average marks')
elif intnum<=100:
    print('A+  good boy') """