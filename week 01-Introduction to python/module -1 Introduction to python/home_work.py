# 1 float kivabeh kaj koreh
""" floattt=input('give me float value : ')
floatvalue=float(floattt)
print(type(floatvalue)) """
# 2 take 3 number from the user and give me the largest number
print('give me 3 number : ')
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
    print(intval3)

