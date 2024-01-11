""" def doubled (num):
    return num*2 """
doubled=lambda num:num*2 # uporer function tah jeh kaj korceh ,ai line tao same kaj tai korche, lambda holo amn aktah system jeath die amrah choto katho function er kaj ai ak line koreh pelteh parih, lambda tah kichu tah list comprehension er motoi.
result=doubled(44)
print(result)

add_3_int= lambda num1,num2,num3:num1+num2+num3 #lambda er moddei maultiple parameter oh caile passed korte parih,just comma, die die passed korte hobhe ar kih
sum=add_3_int(11,11,11)
print(sum)

#map ,this is a built-in function. below line we see some of example
numbers=[10,20,30,30,40,50,50,90,90]
doubled_nums=map(doubled,numbers) #map holoh amn aktah built-in function,jah bujtehi parchi phitronmodule3.8 tekeh ,akhne ai line map a 2 tah property jekhane doubled hocceh aktah function store rakteche 3no. line a,ar ai function tai amrah numbers name jeh list tah nicchi seh list er elemnt gulur upor chalacchi, normally jah bujlam map a 2 tah property takbhe 1st ath hocceh jeh kono aktah function bah operation system ar 2nd tah hocceh operation bah function jetai hok setah jeh jiniser upor apply korbho tah dibho
print(list(doubled_nums))

#filter,this is also a built-in-function ,map kintu kono aktah list,tuples,bah jar upor chalai keno map shob gulo elemnt er upor operation chalbhe,kintu filter tah condition er upor base koreh operation chalbhe and output dibhe, niche aktah dictionary er upor aktah example deoa holoh
actors=[
{'name':'sabana','age':65},
{'name':'sabnoor','age':45},
{'name':'shaonti','age':35},
{'name':'srabonti','age':35},
{'name':'shaon','age':32},
]
juniors=filter(lambda actor:actor['age']<40,actors)
print(list(juniors))