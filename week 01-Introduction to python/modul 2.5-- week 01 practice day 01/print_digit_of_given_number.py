def find_digit(num):
    digit=num%10
    digit=digit/10
    print(digit)

T=int(input('testcase : '))
while T!=0:
    num=int(input('num: '))
    find_digit(num)


