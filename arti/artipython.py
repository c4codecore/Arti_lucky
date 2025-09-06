# print("hello world")
# print("good morning sir ji")
# list1=[10,20,30,40]
# total=0
# for i in list1:
#     total+=i
# avg=total/len(list1)
# print(avg)
# list1=[22,88,98,765,7642]
# min=list1[0]
# for i in list1:
#     if min>i:
#      min=i
# print(min)

# list1=[1,2,3]
# list2=[4,5,6]
# length=len(list1)
# for i in range (length):
#     print(list1[i],list2[i])


# str=input("enter the string:")
# count=0
# for i in str:
#     if i in "aeiou":
#         count+=1
# print("number of vowels:",count)


# x=10
# y=20
# z=x
# x=y
# y=z
# print(x,y)

# list1=[18,99,77,86,54,109,105]
# #for i in list1():
# if list1[0]>list1[1]:
#     largest=list1[0]
#     second_largest=list1[1]
# else:
#     largest=list1[1]
#     second_largest=list1[0]
# for i in range(2,len(list1)):
#     if list1[i]>largest:
#         second_largest=largest
#         largest=list1[i]
#     elif list1[i]>second_largest:
#         second_largest=list1[i]
# print(second_largest)
    

#list1=[18,99,77,86,54,109,105]
list1=[9,8,7,6,5,4]
if list1[0]>list1[1]>list[2]:
    largest=list1[0]
    second_largest=list1[1]
    third_largest=list1[2]
else:
    largest=list1[2]
    second_largest=list1[0]
    third_largest=list1[1]
for i in range(3,len(list1)):
    if list1[i]>largest:
        second_largest=largest
        largest=list1[i]
    elif list1[i]>second_largest:
        second_largest=list1[i]
    elif list1[i]>third_largest:
        third_largest=list1[1]
print("the third largest number:",third_largest)
print("the second largest number:",second_largest)
print("the first largest number:",largest)