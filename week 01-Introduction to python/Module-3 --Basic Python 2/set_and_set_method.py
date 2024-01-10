#set unique items collection,no duplicate,set kintu order tah maintain koreh nah.

# list -->[]
# tule -->()
# set -->{}
numbers=[10,20,30,30,40,50,50,90,90]
print(numbers)
set_ofNumbers=set(numbers)# numbers name a je list tah ache seta keh set a convert korlam.
print(set_ofNumbers)
set_ofNumbers.add(15)# set a number add korah jai
print(set_ofNumbers)
set_ofNumbers.remove(10)#caileh e number remove korah jabhe.
print(set_ofNumbers)
for item in set_ofNumbers:
    print(item)
if 9 in set_ofNumbers:
    print('exist')
else:
    print('no exist')
