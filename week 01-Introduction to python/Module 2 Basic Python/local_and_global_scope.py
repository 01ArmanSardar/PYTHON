#GLobal variable
balance=3000

def buy_things(item,price):
    #you can access global variable without using the global keyword,jodhi tmi variable tah function parameter hisebhe pass koro ar kih
    #if you want to modify a global varaible ,you have to use the global keyword
    global balance
    print(f'previous balance value',balance)
    balance=balance-price
    print(f'balacne after bye {item}',balance)

buy_things('sunglass',1000)
