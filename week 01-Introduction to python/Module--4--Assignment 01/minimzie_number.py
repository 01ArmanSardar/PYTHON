def max_oprt(N, A):
    max_ops=0
    while all (x%2==0 for x in A):
        index=0
        while index<len(A):
            A[index] =A[index]//2
            index +=1
        max_ops +=1
    return max_ops
N=int(input())
A=list(map(int,input().split()))
result=max_oprt(N,A)
print(result)