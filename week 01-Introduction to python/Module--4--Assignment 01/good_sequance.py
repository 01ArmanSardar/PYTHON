def find_good_sequance(N,A):
    count_dict={}
    for x in A:
        count_dict[x]=count_dict.get(x,0)+1
    total_removed=0
    for x,count in count_dict.items():
        exxcess_ocurrences=max(0,count-x)
        total_removed+=exxcess_ocurrences
    return total_removed
N=int(input())
A=list(map(int,input().split()))
result=find_good_sequance(N,A)
print(result)

