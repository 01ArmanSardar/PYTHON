# in ,not ,not in ,is ,is not 

""" a=2
if a>5:
    print('5 er beshi')
elif a==2:#python a else if keh short-from koreh   elif   likha hoi
    print('2 er soman')
else:
    print('5 er kom') """

boss =False
""" if boss is True:
    print('boss keh thel diteh jacchi')
else :
    print('akhn time nai') """
""" if boss is not True:
    print('akhn time nai')
else :
    print('boss keh thel diteh jacchi') """

#nasted conditons 
coin ='head'
if boss==False:
    print('boss you are joos')
    if coin=='tail':
        print('batting')
    else:
        print('balling')
else:
    print('boss is not good')
    