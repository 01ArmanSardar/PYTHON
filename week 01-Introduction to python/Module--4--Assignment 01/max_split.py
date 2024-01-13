def find_balance_string(S):
    count_l=0
    count_r=0
    current_str=""
    total_str=0
    for char in S:
        if char=='L':
            count_l=count_l+1
        elif char=='R':
            count_r=count_r+1
        current_str=current_str+char
        if count_l==count_r:
            total_str=total_str+1
            print(current_str)
            current_str=""
    print(total_str)
    

S=input()
find_balance_string(S)