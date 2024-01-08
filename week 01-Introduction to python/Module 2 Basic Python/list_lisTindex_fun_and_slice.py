#index=   0  1   2   3   4   5   6   7   this indexing is forward and positive
numbers=[45, 56, 23, 62, 89, 54, 12, 67]
#index =  -8  -7  -6 -5  -4  -3  -2  -1  this indexing is bakward and negative 

print(numbers[3],numbers[-3]) #akhne 62 abong 54 duitai print hobhe.

#list[start_index : end_index] #below line print the list,    start from the start index and stops before the end index
print(numbers[2:5])

#list[start_index :end_index :step] #step manhe koitah index por por print korbho
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[7:2:-1])#maneh 7 index tekeh 2 index er dikeh jabho

print(numbers[:6])#akhne amra sudhu end index dichi start index dei nai kintu python by default start index prothom tekeh dhore niceh
print(numbers[1:])#akhne amra sudhu start index dichi end index dei nai kintu python by default end index sesh projontho dhore niceh
print(numbers[:])#jodhi start and end index kono tai nah dei tahole puro list tai print hoie jabhe

print(numbers[::-1])#shortcut to reverse a list.