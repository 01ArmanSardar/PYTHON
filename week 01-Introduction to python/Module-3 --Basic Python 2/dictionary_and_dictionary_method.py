# dictionary er 2tah part key and value, atakhe key value pair oh bolah jai
# structure of a dictionary -->  {key:value, key:value, key:value, key:value}
person={'name':'arman','roll':'19','class':'nine','school':'arun school'}
print(person) # puroh dictionary tai print korlam.
print(person['name'])#akhne tah teh name holo aktah key ,print korlam arman key er value tah
print(person.keys())#akhan tah teh person dictionary er sudhu keys gulah print korlam
print(person.values())#akhan tah teh person dictionary er sudhu values gulah print korlam
person['languages']='python'#akhne person dictionary teh notun aktah key value jogh korchi
print(person)
person['name']='minara'#caileh kono aktah keys er value modify korah jabhe
print(person)
del person['roll']# dictionary er kono aktah keys chailei delete korah jabhe.
print(person)

#special dictionary looping
for key ,value in person.items(): # onnano for loop gular cehe dictionary er upo chalano for loop aktu binnhho ar kih.
    print(key,value)