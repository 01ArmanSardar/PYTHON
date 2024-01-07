""" print('now i need money')
input() """
# input('Give some money: ')
""" money=input('give some money')
print(money) """
first_money=input('kodom ali ,dosto kichu tk deh : ')
second_money=input('setu apah kichu tk deh : ')
print(type(first_money))
#by default the input form user will be string type , uporeh amrah first money and second money by default string type pabho ,jemon amrah jodhi first money 100 ar second money 200 nei tahole first money and second money + korle 100200 asbeh,karon input tah by defult string hisebhe neoa hoieche
print('money i got from kodom ali ',first_money,'and from setu',second_money)
# total=first_money+second_money
# print('total money i got', total)
first_money_int=int(first_money)
second_money_int=int(second_money)
print(type(first_money_int))
total=first_money_int+second_money_int
print('total money i got',total)