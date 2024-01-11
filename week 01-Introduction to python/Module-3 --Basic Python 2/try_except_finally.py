try:
    result=45/0 #akhne 45/0 run korle kintu normally error asbhe ,abong program run korle crash korbhe abong tkhn ai line er niche onnao valid operation takleh oh setah kintu output diteh parbhe nah,tobhe amrah jodhi try abong except ai 2 tah keyword use kori tahole ar error tah asbeh nah, abong ami nicher valid operation gulah korteh parbho
except:
    print('error happened')
finally:
    print('finally here')# amrah jodhi monhe kori kono aktah line bah function a error asteh pareh tahole seh lin er jonno amrah try use korbho,jodhi sekhne error takhe tahole setah except ai chole jabhe ,ar jodhi finally use korih tahole ,error takleh oh akhne asbhe nah takleh oh akhne asbhe.
print('done')