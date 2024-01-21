def find_digit(num):
    reversed_str=str(num)[::-1]
    print(' '.join(reversed_str))

T=int(input('testcase : '))
while T!=0:
    num=int(input('num: '))
    find_digit(num)
    T=T-1
