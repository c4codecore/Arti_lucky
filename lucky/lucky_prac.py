print("hello World")
print("ok")
# print always take currenty value not old for exp.
# a=10
# a=20
# print(a) # jaise es mei print value 20 lega instead of 10.

# li=[10,20,30,40,60]
# min=li[0]
# for i in li:
#    if i<min:
#     min=i
# print(min)
# max=li[]
# li1=[1,2,3]
# li2=[4,5,6]
# length=len(li1)
# for i in range(length):
#     print(li1[i],li2[i])

# # for i in li1:
#   if i in li2:
#     print(i)
li=[100,200,300,500,600]
max=li[0]
max2=li[1]
for i in li:
    if i>max:
        
        max=i
    elif i>max2 and i!=max:
        max2=i
print(i)

# Elephant

# vowels count
a=10
b=20
if a>b:
    max=a
    min=b

else:
    max=b
    min=a
print(max)
a=10
b=20
c=30
first=0
second=0
third=0
if a>b and a>c:
    first=a
    if b>c:
        second=b
        third=c
    else:
        second=c
        third=b     
elif b>a and b>c:
    first=b
    if a>c:
        second=a
        third=c
    else:
        second=c
        third=a
elif c>b and c>a:
    first=c
    if b>a:
        second=b
        third=a
    else:
        third=b
        second=a
print(first,second,third)


password=""
while password != "password123":
  password=input("Enter password : ")
print("Access Granted")




