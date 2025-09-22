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
    # list1=[18,99,77,86,54,109,105]

# largest=list1[0]
# second_largest=list1[1]
# third_largest=list1[2]
# if list1[0]>list1[1]and list1[0]>list1[2]:
#     largest=list1[0]
#     if list1[1]>list1[2]
#     second_largest=list1[1]
#     third_largest=list1[2]
#     else:
#     second_largest=list1[0]
#     third_largest=list1[1]
# elif list1[2]>list1[0]and list1[2]>list[1]   
#       if list1[0]>list1[]
# for i in range(3,len(list1)):
#     if list1[i]>largest:
#         second_largest=largest
#         largest=list1[i]
#     elif list1[i]>second_largest:
#         second_largest=list1[i]
#     elif list1[i]>third_largest:
#         third_largest=list1[1]
# print("the third largest number:",third_largest)
# print("the second largest number:",second_largest)
# print("the first largest number:",largest)

# x=10
# y=20
# z=30
# first=0
# second=0
# third=0
# if x>y and x>z:
#     first=x
#     if y>z:
#         second=y
#         third=z
#     else:
#         second=z
#         third=y
# elif y>z and y>x:
#     first=y
#     if x>z:
#         second=x
#         third=z
#     else:
#         second=z
#         third=x
# elif z>x and z>y:
#     first=z
#     if x>y:
#         second=x
#         third=y
#     else:
#         second=y
#         third=x
# print(first)
# print(second)
# print(third)
     

# i=2
# while i<=20:
#  print(i)
#  i=i+5

# n=int(input("enter the number:"))
# total=0
# i=1
# while i<=n:
#     total+=i
#     i+=1
# print("the sum of number: 1 to",n,"__",total)


# password=""
# while password !="arti1234":
#     password = input("enter the passward:")
# print("correct passward successful enter")

# for i in range(1,100):
#     if i%2==0:
#         print(i)
# i=1
# while i<=100:
#     if i%2==0:
#         print("even number:",i)
#     i=i+1

# i=1
# count=0
# while i <=100:
#     if i%2==0:
#         count+=1
#     i=i+1
# print(f"total even numbers from 1 to 100 is: {count}")

# i=1
# sum=0
# while i<=100:
#     if i%2==0:
#         sum+=i
#     i=i+1
# print(f"sum of all even numbers 1 to 100: {sum}")

# i=1
# total=0
# count=0
# while i<=100:
#     if i%2==0:
#         total+=i
#         count+=1
#     i=i+1
# # print(total,count)
# print(f"avg number 1 to 100 : {total/count}")

# i=5
# while i >=1: 
#     print(i)
#     i=i-1

# i=10
# while i>=1:
#     if i%2==0:
#         print(i)
#     i=i-1

# i=10
# count=0
# while i>=1:
#     if i%2==0:
#        count+=1
#     i=i-1
# print(f"even number :{count}")
    
# i=10
# total=0
# while i>=1:
#     if i%2==0:
#         total+=i
#     i=i-1
# print(f"the total of even number:{total}")

# i=10
# total=0
# count=0
# while i>=1:
#     if i%2==0:
#         total+=i
#         count+=1
#     i=i-1
# print(f"avg number of even :{total/count}")

# a =""
# while a != "exit":
#         a = input("please enter something :")
#         print(f"you have entered :{a}")
# print("sucessfuly exit")

# print("=======MENU=======")
# print("A:greet")
# print("B:show course list:")
# print("C:show center details:")
# print("D:contact information:")
# print("E:exit")
# choose=input("enter the option: ")
# match choose:
#     case "A":
#         print("hello welcome to code core computer center")
#     case "B":
#         print("courses offerd")
#         print("1:basic computer course")
#         print("2:python programming")
#         print("3:web desigining")
#         print("4:data analytics")
#     case "C":
#         print("code core computer center:established in 2024,specialized in it courses")
#     case "D":
#         print("contact number:9013010909")
#     case "E":
#         print("thank you! goodbye")
#     case _:
#         print("invalid choice.please select between A to E.")

# while True:
#     print("=======MENU=======")
#     print("A:greet")
#     print("B:show course list:")
#     print("C:show center details:")
#     print("D:contact information:")
#     print("E:exit")
#     choose=input("enter the option: ")
#     match choose:
#         case "A":
#             print("hello welcome to code core computer center")
#         case "B":
#             print("courses offerd")
#             print("1:basic computer course")
#             print("2:python programming")
#             print("3:web desigining")
#             print("4:data analytics")
#         case "C":
#             print("code core computer center:established in 2024,specialized in it courses")
#         case "D":
#             print("contact number:9013010909")
#         case "E":
#             print("thank you! goodbye")
#             break
#        case _:
#            print("invalid choice.please select between A to E.")
# exit=""
# while exit!="exit":
#     print("=======MENU=======")
#     print("A:greet")
#     print("B:show course list:")
#     print("C:show center details:")
#     print("D:contact information:")
#     print("E:exit")
#     choose=input("enter the option: ")
#     match choose:
        # case "A":
        #     print("hello welcome to code core computer center")
        # case "B":
        #     print("courses offerd")
        #     print("1:basic computer course")
        #     print("2:python programming")
        #     print("3:web desigining")
        #     print("4:data analytics")
        # case "C":
        #     print("code core computer center:established in 2024,specialized in it courses")
        # case "D":
        #     print("contact number:9013010909")
        # case "E":
        #     print("thank you! goodbye")
        #     exit="exit"
        # case _:
        #    print("invalid choice.please select between A to E.")

# x=-1
# if x:
#     print("watter bootle")
# else:
#     print("coffee mug")


# for i in range(3):
#   print("for loop start",i)
#   for j in range(5,7): 
#        print("inside loop",i,j)
#   print(i)

# attempts=0
# while attempts<3:
#     passward=input("enter passward:")
#     if passward=="python123":
#         print("access granted!")
#         break
#     attempts+=1
# else:
#     print("too many failer attempts")

# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         print("not prime number")
#         break
# else:
#     print("prime number",num)


# flag=True
# num=int(input("enter the number:"))
# for i in range(2,num):
#     if num%i==0:
#         flag=False
#         break

# # if flag:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is  not prime")

# result=f"{num} is a prime number" if flag  else f"{num} is  not prime"
# print(result)

# i=0
# num=int(input("enter the number:")) 
# while num>=i: 
#     print(i)
#     i+=1


# i=1
# num=int(input("enter the number:"))
# while num%2==0:
#     print(f"{i}is a even number:")
#     i+=1
# # else:
# #     print(f"{i}is a odd number:")

# i=1
# num=int(input("enter the number:")) #8
# while num>=i: 
#     if i%2: #1%2=1 true ,2%2 =0 false
#         print(i)
#     i+=1
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#    for j in range(1,n+1):
#     print(n+1-j,end=" ")
#    print() 
 
# n=int(input("enter the number:"))
# for row in range(1,n+1):
#     for col in range(1,n+1):
#         print(row,col,sep="",end=" ")
#     print()

# for i in range(2):
#     for j in range(2):
#         for k in range(2):
#             print(i,j,k)

# i=1
# while i <=3:
#     j=1
#     while j<=3:
#         print(i,j)
#         j+=1
#     i+=1