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
# print(my_string.index())

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


str1="hello"   
str2="123" 
str3=len(str1)
str4=len(str2)
if str3>str4:
    max=str1
    min=str2 
else:
    max=str2
    min=str1
res=""
for i in range(len(min)):
    res+=str1[i]+str2[i]
res+=max[len(min):]
print(res)

    


