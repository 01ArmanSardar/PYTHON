""" list =[]
list = input().split() """
n = int(input())
a = list(map(int, 
    input().strip().split()))[:n]
""" n=int(input())
for i in range(0,n):
    ele=int(input())
    list.append(ele) """
list2=list[::-1]
""" list_len=len(list)
print(list_len) """

if list==list2:
    print('YES')
else:
    print('NO')
