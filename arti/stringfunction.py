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
str=input("enter the string :")
res_char=""
res_num=""
res_special="" 
res_capital=""
for i in str:
    if  i.isdigit():
        res_num+=i
    elif i in ("@#$%&!^"):
        res_special+=i
    elif i.isalpha():
        if i.isupper():
            res_capital+=i
        elif i.islower():
            res_char+=i
print("Digit in this string :",res_num)
print("special char in this string :",res_special)
print("capital char  in this string :",res_capital)
print("smaller char in this string :",res_char)
    


