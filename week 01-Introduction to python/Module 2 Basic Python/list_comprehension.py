numbers=[45,87,96,65,43,90,85,14,26,61,70]
odds=[]
for num in numbers:
    if num%2==1 and num%5==0:
        odds.append(num)
print(odds)

odd_nums = [num for num in numbers if num % 2 ==1 and num% 5==0]# a line tah kei muloto list comprehension bolah hoie takhe,manhe aktah list er moddei shob kichu 
print(odd_nums)