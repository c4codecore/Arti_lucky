# my_string="gm sir"
# print(my_string.title())

# my_string="gm sir"
# print(my_string.capitalize())

# my_string="gm sir"
# print(my_string.swapcase())

# my_string="gm sir"
# print(my_string.lower())


# my_string="gm sir"
# print(my_string.upper())

# my_string="gm sir"
# print(my_string.strip())

# my_string="gm sir"
# print(my_string.lstrip())

# my_string="gm sir"
# print(my_string.rstrip())

# my_string="gm sir"
# print(my_string.find())

# my_string="gm sir"
# print(my_string.rfind())

# my_string="gm sir"
# print(my_string.index())

# my_string="gm sir"
# print(my_string.index())

# my_string="gm sir"
# print(my_string.index("gm"))

# my_string="gm sir"
# print(my_string.rindex())

# my_string="gm sir"
# print(my_string.startswith())

# my_string="gm sir"
# print(my_string.endswith())

# my_string = "Python123"
# print(my_string.isalnum())  

# print(f"|{'Python':<10}|")  
# print(f"|{'Python':>10}|")
# print(f"|{'Python':^10}|")  

# word=input("enter a word:")
# vowels=0
# consonante=0
# for char in word :
#         if char.lower() in "aeiou":    #A=aeiou false a=aeiou true
#                  vowels+=1
#         elif char in ", .?/|@#":
#                 pass
#         else:
#                 consonante+=1
# print(f"total number of vowels {vowels}, total number of consonate {consonante}")
                
# str1="hello"   
# str2="123" 
# str3=len(str1)
# str4=len(str2)
# if str3>str4:
#     max=str3
#     min=str4  
# else:
#     max=str4
#     min=str3
# res=""
# for i in range(min):
#     res+=str1[i]+str2[i]
# print(res)


# str1="hello"   
# str2="123" 
# str3=len(str1)
# str4=len(str2)
# if str3>str4:
#     max=str1
#     min=str2 
# else:
#     max=str2
#     min=str1
# res=""
# for i in range(len(min)):
#     res+=str1[i]+str2[i]
# res+=max[len(min):]
# print(res)

# char=input("enter a string:")
# word=''
# i=len(char)-1
# while(i>=0):
#     word=word+char[i]
#     i=i-1
# print("enter original string=",char)
# print("enter the reverse string=",word)


# char=input("enter a string:")
# word=''
# len_char=len(char)
# for i in range(1,len_char+1):
#      word=word+char[-i]
#     #  i=i-1
# print("enter original string",char)
# print("enter the reverse string=",word)

# name="arti"
# print(name[2:2])

# name="arti"
# print(name[: : -1 ])

# char=input("enter a string:")
# print(char[: : -1 ])


# str="banana"
# res="" 
# for i in str:     # banana 
#     if i not in res:
#         res+=i
# print("remove duplicate in string",res)

# a=input("enter the string :")   
# if a==a[: :-1]:
#     print("this string is palindrom")
# else:
#     print("this string is not palindrom")

# str=input("enter the string :")
# str2=str.split()
# len_str2=len(str2)
# print(len_str2)

# str="mobile number 88675439"
# res=""
# for char in str: 
#     if char in  "0123456789":
#         res=res+char
# print("number of digit ",res)


# str="email:xyz123@gmail.com"
# idx=str.index("@")
# username=str[0:idx]
# domain=str[idx+1:]
# print(username,domain)


# str="xyz123@gmail.com"
# for i in range(len(str)):  
#     char = str[i]
#     if char in "@": #@=@
#         idx=i 
#         break  
# username=str[0:idx]
# domain=str[idx+1:]
# print(username,domain)

# a=int(input("enter the number :"))
# for a in range(10,20):
#     if a%2:       
#         print("even number: ",a)
    

# str="hello world"
# res="" 
# count=0
# for i in str:     # hello world
#     if i not in res and i.isalnum():
#         res+=i
#         count+=1
# print("remove duplicate in string",res, count)




# str=input("enter the string :")
# res="" 
# vowels="aeiou"
# for i in str:     # hello world
#     if i not in vowels:
#         res+=i
# print("remove duplicate in string",res)

# str="Aaiou HEELO 8@78$8dh9 gf#dAA"
# str=input("enter the string :")
# res_char=""
# res_num=""
# res_special="" 
# res_capital=""
# for i in str:
#     if  i.isdigit():
#         res_num+=i
#     elif i in ("@#$%&!^"):
#         res_special+=i
#     elif i.isalpha():
#         if i.isupper():
#             res_capital+=i
#         elif i.islower():
#             res_char+=i
# print("Digit in this string :",res_num)
# print("special char in this string :",res_special)
# print("capital char  in this string :",res_capital)
# print("smaller char in this string :",res_char)

# a=[10,20,30,40]
# b=a[0]
# print(b)

# a=[10,[10,20],30,50,60]
# b=a[1] #[10,20]
# print (b[1]) #output=20


# a=[10,[10,20],30,50]
# print(a[1][1])

# a=list(range(0,10,2))
# print(type(a))

# a=list({"good_morning": "dear_sir",})
# print(a)
# print(type(a))
    

# a=eval(input("enter the list :"))
# print(a)
# print(type(a))

# a="python language is very easy :"
# a=a.split()
# print(a)
# print(type(a))


# a=[]
# print(a)

# a=list(10)
# #print(a)

# list1=list("python")
# print(list1)

# list1=[10,33,77,77,88,98]
# print(list1.count(77))

# l=[10,94,87,87,38,8765]
# print(l.count(87))


# l=[98,76,55,87,00,43]
# print(l.index(55))

# L1=["A","B","C","D"]
# L2=["E","F","G","H"]
# L1.append(L2)
# print(L1)


# L1=["A","B","C","D"]
# L2=["E","F","G","H"]
# L1.extend(L2)
# print(L1)


# L1=["A","B","C","D"]
# L1.remove("B")
# print(L1)

# L1=['A','B','C','D']
# L1.pop(1)
# print(L1)

# L1=[11,22,33,44,55,66,77]
# L1.reverse()
# print(L1)


# L1=["A","B","C","D"]
# l2=L1[:]
# print(l2)

# L1=[11,22,33,44,55,66,77]
# print(55 in L1)

# L1=[11,22,33,44,55,66,77]
# print(77 not in L1)

# list1=[88,99,5,6,7]
# cube=[i*i*i for i  in list1]
# print(cube)

# even=[i for i in range(1,11) if i%2==0]
# print(even)

# odd=[i for i in range(1,11)if i%2]
# print(odd)

# list1=[char for char in "code core computer center" ]
# print(list1)


# word="code core computer center".split()
# print(word)
# res=[(w.upper(),len(w)) for w in word]
# print(res)

# vowels="a,e,i,o,u"
# word=input("enter the word :")
# result=[]
# [result.append(char) for char in word if char in vowels if char not in result]
# print(result)


# cities=["mumbai","delhi","gurugram","pune"]
# for city in cities:
#     print(city)

# numbers=eval(input("enter the list of numbers: "))
# for num in numbers:
#     if num%2==0:
#         print(num)

# list1=[10,20,30,40,50,60,70]
# list1.insert(4,88)
# print(list1)


# a=[1,3,4]
# b=[3,7]
# print(a+b)
# print(b+a)
# print(a*2)

# a=[1,3,4,5,6,7,8,9]
# print(a[1:4])
# print(a[:3])
# print(a[::2])

# t=(10, 20, 30, 40) 
# print(type(t))
# l=list(t)
# print(l)

# word="code core computer center".split()
# print(word)

# list1=['A','B','C']
# list2=['D','E','F']
# list3=['G','H','I']
# print(list1==list2)
# print(list2!=list3)
# print(list1==list3)


# number=[10,20,30,40,50]
# largest_num=number[0]
# for num in number:
#     if num>largest_num:
#         largest_num=num
# print(largest_num)

# number=[67,89,10,20,30,40,50]
# smallest_num=number[0]
# for num in number:
#     if num<smallest_num:
#         smallest_num=num
# print(smallest_num)


# number=[67,89,10,20,30,40,50]
# smallest_num=float('inf')
# for num in number:
#     if num<smallest_num:
#         smallest_num=num
# print(smallest_num)

# number=[67,89,10,20,30,40,50]
# number.sort()
# print(number)
# print(number[-1])

# a=[11,22,33,44,55,33,22]
# b=[]
# for i in a:
#     if  i not in b:
#         b.append(i)
# print(b)

# list1=['abs','aba','aa','a']
# list2=[]
# count=0
# for i in list1:
#     if len(i)>=2:
#        if i[0]==i[-1]:
#             count+=1
#             list2.append(i)
# print(count,list2)


# list1=[]
# if list1==[]:
#     print("true")
# else:
#     print("false")

# list1=[10,66,8,9,7]
# if list1:
#     print("false")
# else:
#     print("true")


# list_str=['apple','banana','pear','grapes']
# list_str2=[]
# count=0
# for i in list_str:
#     if len(i)>4:
#         count+=1
#         list_str2.append(i)
# print(count,list_str2)


# list1=[1,2,3,4,5]
# list2=[6,7,8,9,2]
# for i in list1:
#     if i in list2: #1
#         print("yes")
#         break

# list1=[1,2,3,4,5]
# list2=[6,1,8,5,3]
# list3=[]
# count=0
# for i in list1:
#     if i in list2:
#         count+=1
#         list3.append(i)
# print(count,list3)


# a=["123abscd"]
# alp=[]
# num=[]
# for char in a:
#     if char.isalpha():
#         alp.append(char)
#     else:
#         num.append(char)
# alp.sort()
# num.sort()
# print(alp,num)


tup=(10,20,30,40,50)
li=list(tup)
li.reverse()
tup=tuple(li)
print(tup)
