# tuples are immutable
""" def multiple():
    return 3,4
print(multiple())# lsit hocche [3rd backet] die ar tuple hocceh (first backet) die. """

things='pen','tripod','camera','phone number','sunglass','charger','watch' #ata kei normally tupke bolhe takhe.
print(type(things))
print(things[1])# tuple er 1th index tah print korbhe,list er motoi ar kih/
print(things[-2]) # last er dikh tekeh 2th index tah print korbhe.
print(things[1:5]) # slice korlam,manhe 2th index teekh 5th index projnto print korlam
print(things[::]) #normal print korlam.
print(things[::-1]) #reversed print korlam.

if 'phone number' in things: #kono aktah kichu tuple er moddeh ache kina tah chcek kora jai
    print('exist.')
else:
    print('not exist.')

for item in things:
    print(item)

