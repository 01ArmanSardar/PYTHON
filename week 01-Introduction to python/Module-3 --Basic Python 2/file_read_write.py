#  .csv comma separated value
#  .txt text file

""" with open('message.txt','w') as file: # current program tekeh notun akath text file create korlam ai folder er vitorei,abong sekhane 'i love,python' lekha uthbhe,
    file.write('i love ,python') """

""" with open('message.txt','a') as file: # ai line tah tekeh amra message.txt name jeh file tah create korbho setah 'i love,python' tai abr append korte parbho varbar,tr jonnno message.txt er upor a liklam, ager line e w chilo karon sekhane write korte chilam
    file.write('i love ,python') """

with open('message.txt','r') as file:
    text=file.read()
    print(text)