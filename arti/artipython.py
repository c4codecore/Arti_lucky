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




from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

#DEVELOPED BY Mark Arvin
root = Tk()
root.title("Contact List")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")

#============================VARIABLES===================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS = StringVar()
CONTACT = StringVar()



#============================METHODS=====================================

def Database():
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT)")
    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def SubmitData():
    if  FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS.get() == "" or CONTACT.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (firstname, lastname, gender, age, address, contact) VALUES(?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS.get()), str(CONTACT.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")

def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `firstname` = ?, `lastname` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact` = ? WHERE `mem_id` = ?", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS.set("")
        CONTACT.set("")
        
    
def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    AGE.set(selecteditem[4])
    ADDRESS.set(selecteditem[5])
    CONTACT.set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()

    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=5, column=1)
    

    #==================BUTTONS==============================
    btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)


#fn1353p    
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
    
def AddNewWindow():
    global NewWindow
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS.set("")
    CONTACT.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Contacts", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="Firstname", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Lastname", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)

    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=AGE,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=ADDRESS,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=CONTACT,  font=('arial', 14))
    contact.grid(row=5, column=1)
    

    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)




    
#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="#6666ff")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#6666ff")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(Top, text="Contact Management System", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#============================ENTRY=======================================

#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+ ADD NEW", bg="#66ff66", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)

#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()
    
