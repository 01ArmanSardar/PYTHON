def full_name(first,last):
    name=f'full name is: {first}{last}'
    return name
#below line take parameters in order(serial wise)
# name=full_name('alu ','kodu')
name = full_name(last='kodu ',first='alu ')#python serial wise parameter nah dileo chole ,sudhu function parameter belai e nah,python er arkm onk jaigai e serial mainatain nah korleo output thik e ashe
print(name)
#................
""" def famous_name(first,last,**adition):#   **adition   ai jinish tah keh kargs bolah hoie takhe ,maneh fuction parameter er aghe 2ta ** dile setah keh kargs bolhe, kargs a prothi tah args er aghe aktah key takhe tai atake kargs boleh  
    name=f'{first} {last} '
    # print(adition)
    for key,value in adition.items():#ai line tah teh amrah  **adition  je kargs nilam ,setha tekhe key abong value gulah bher koreh pellam tarpor nicher line a
        print(key,value) #print koreh dilam ,example jmn  title='hujur  ,akhne title tah holo key ar hujur tah holo value
    return name
name=famous_name(first='taher',last='ali',title='hujur',upadhi='madani')
print(name) """
#...................
# def function_name(num1 , num2 , *args , **kargs): ai line tah niceh explain krlm
#def function name(aktai parameter, aktai parameter, onkgulu parameter, onkgulu parameter sateh abong sateh parameter gulur aktah key o ache)
#...................
def a_lot(num1,num2):
    sum=num1+num2
    multi=num1*num2
    remain=num1-num2
   # return [sum,multi,remain]  amrah caile avabhe rerurn korte parhi, avbhe pataleh by default akta list hisebhe return hobhe ans gulu
    return sum,multi,remain
everything=a_lot(20,10)
print(everything)