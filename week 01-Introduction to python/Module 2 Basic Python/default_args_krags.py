""" def sum(num1,num2,num3=0):
    result=num1+num2
    return result
total=sum(10,20,90)
print('total : ',total) """
#args
""" def all_sum(*numbers):#  *numbers , Atah keh tuple bolah hoi,manhe function e parameter er aghe akta * sign dilei hoie jabhe,ata likhe jodi amrah multiple parameter passed korih tahole function setha nite parbhe,atah kind of list bah array er moto kaj koreh takhe
    print(numbers)
    for num in numbers:
        print(num)

total=all_sum(45,47,89,11)
print('all sum : ',total) """
def all_sum(num1,num2,*numbers):# 
    print(numbers) 
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
    return sum

total=all_sum(10,20,30,40,50,60)
print('all sum : ',total)