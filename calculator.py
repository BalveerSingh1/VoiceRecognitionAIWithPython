from tkinter import *
from tkinter import messagebox

Screen=Tk()
Screen.title("Registration Form")
Screen.geometry("400x400")
Screen.resizable(False,False)

def Register():
    Name=NameInfo.get()
    Age=AgeInfo.get()
    Phone=PhoneNOInfo.get()
    Email=EmailInfo.get()

    if(len(Name) == 0):
            # print(name)
            messagebox.showerror("Error" , "Please enter your name")
            
    elif (len(Age) == 0):
            print(Age)
            messagebox.showerror("Error","Please enter your age")
    elif (len(Phone) == 0):
            print(Phone)
            messagebox.showerror("Error","Please enter your phone no")
    elif (len(Email) == 0):
            print(Email)
            messagebox.showerror("Error","Please enter your Email Id")
    else:
            Label(Screen,text="Registration Sucessful",font="20",fg="green").place(x=135,y=285)
    with open(Name+".txt","w")as f:
           f.write(Name+"\n")
           f.write(Age+"\n")
           f.write(Phone+"\n")
           f.write(Email+"\n")
           
def Clear():
    NameEntry.delete(0, END)
    AgeEntry.delete(0, END)
    PhoneNOEntry.delete(0, END)
    EmailEntry.delete(0, END)
  
# label 
Label(Screen,text="Registration From",font="ariel 20 bold",bg="red",fg="black",).pack(fill="both")
Label(Screen,text="Name",font="20").place(x=35,y=75)
Label(Screen,text="Age",font="20").place(x=35,y=110)
Label(Screen,text="Phone No",font="20").place(x=35,y=145)
Label(Screen,text="Email Id",font="20").place(x=35,y=180)

# input 
NameInfo=StringVar()
AgeInfo=StringVar()
PhoneNOInfo=StringVar()
EmailInfo=StringVar()
NameEntry=Entry(Screen,font="10",bd="4",textvariable=NameInfo)
NameEntry.place(x=140,y=75)
AgeEntry=Entry(Screen,font="10",bd="4",textvariable=AgeInfo)
AgeEntry.place(x=140,y=110)
PhoneNOEntry=Entry(Screen,font="10",bd="4",textvariable=PhoneNOInfo)
PhoneNOEntry.place(x=140,y=145)
EmailEntry=Entry(Screen,font="10",bd="4",textvariable=EmailInfo)
EmailEntry.place(x=140,y=180)
Button(Screen,text="Register",font="20",command=Register).place(x=185,y=225)
Button(Screen,text="Clear",font="20",command=Clear).place(x=325,y=355)

mainloop()
































# # # wind.mainloop()
# win=Tk()
# wind.title("calculator")
# wind.geometry("300x400")
# text=Entry(wind,font=("calibri",16))
# text.pack(fill=X,padx=5,pady=5,ipadx=5,ipady=5)
# frame=Frame(wind)

# frame.pack(side=TOP,anchor=NW)
# rightFrame= Frame(frame)

# rightFrame=Frame(frame)
# frame.pack(side=RIGHT)

# frame1=Frame(frame)
# frame1.pack()

# #button 1 to 3
# btn1= Button(frame1,text="1",width=9,height=3)
# btn1.pack(side=LEFT)

# wind.mainloop()


