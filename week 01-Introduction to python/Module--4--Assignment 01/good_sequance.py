def find_good_sequance(N,A):
    A.sort()
    total_removed=0
    for i,x in enumerate(A,start=1):
        excess=max(0,i-x)
        total_removed+=excess
    return total_removed
N=int(input())
A=list(map(int,input().split()))
result=find_good_sequance(N,A)
print(result)

