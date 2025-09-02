li=[10,20,30,40]
length = len(li) # 4

for i in range(length-1, -1, -1): # 3 2 1 0
    print(li[i])

for i in range(1, length+1): # 1 2 3 4
    print(li[-i])


-3 -2 -1 0 1 2 3 4 5 6

# range left se right means positively ---> end-1
# range right se left means negatively ---> end+1