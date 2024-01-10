name='shakib khan'#Avbhe string declare kordah jai 
name0='Sakib\'s khan'# escape
name2="sakib khan tush " #Avhabeo string declare korah jai
name3=""" 
shakib khan number 3,
faltoh naoyk shakib kahn
""" #avbhe o multiline coment er moto kore string declare korah jai
print(name0)

# string is a sequence of characters.
for char in name2:# name 2 er shob gulah charcater bher koreh print korlam.
    print(char)
print(name2[3])#name2 string er 3th index er value tah print korlam.
print(name2[1:6]) #slice korlam,1th index tekeh 6th index aladah korlam.
print(name2[-3]) #list er moto string e oh avbhe negative and backward index kaj koreh.
print(name2[::-1]) #list er moto string e oh avbhe reverse korah jai.
if 'khan' in name2: #string er moddeh kono aktah jinish ache kinah setah check korah jai
    print('exists')
# mutable means changable ,for example list.
# immutable means you can not change it ,for example string.