# li=[10,20,30,40]
# length = len(li) # 4

# for i in range(length-1, -1, -1): # 3 2 1 0
#     print(li[i])

# for i in range(1, length+1): # 1 2 3 4
#     print(li[-i])


# -3 -2 -1 0 1 2 3 4 5 6

# range left se right means positively ---> end-1
# range right se left means negatively ---> end+1



# 3 Sept 2025

# li = [100,20,150,125,200,15,150,99]
# max = li[0]

# for i in li:  
#     if i > max:  
#         max = i

# print(max)


# Elephant

# vowels count

# li_1= [1, 2, 3]
# li_2= [4, 5, 6]

# length = len(li_2) # 3

# for i in range(length): # 0 1 2 

# 1 4
# 2 5
# 3 6

# 1) git pull
# 2) message--> commit --> sync


li = [10,20,30,25,24,45]

if li[0] > li[1]:
    largest = li[0]
    second_largest = li[1]
else:
    largest = li[1]
    second_largest = li[0]

for i in range(2, len(li)): 
    if li[i] > largest:  
        second_largest = largest
        largest = li[i]
    elif li[i] > second_largest:
        second_largest = li[i]