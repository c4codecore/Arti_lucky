# tup = (10, 20, 30, 40)
# item_to_remove = 30
# li = list(tup) # [10, 20, 30, 40]
# li.remove(item_to_remove) # [10, 20, 0]
# tup = tuple(li) # (10, 20, 40)
# print(tup) # (10, 20, 40)

# tup = (10, 20, 30, 40)
# item_to_find = 30
# idx = tup.index(item_to_find)
# print(idx)

# tup = (10, 20, 30, 40)
# item_to_find = 300
# idx = tup.index(item_to_find)
# print(idx)

# list_of_tuples = [(1, 2), (3, 4), (5, 6)]
# li0=[]  # [1,3,5]
# li1=[]  # [2,4,6]
# for ele in list_of_tuples: # (5,6)
#     li0.append(ele[0])
#     li1.append(ele[1])

# tup0= tuple(li0) # (1,3,5)
# tup1= tuple(li1) # (2,4,6)

# res = [tup0, tup1] # [(1,3,5), (2,4,6)]
# print(res)


# list_of_tuples_1 = [(1, 2), (2, 3), (3, 4)]
# res=[]
# for tup in list_of_tuples_1:
#     sum = tup[0] + tup[1]
#     res.append(sum)
# print(res)


# li = []
# li.append(10)
# print(li)
# li.append(20)
# print(li)