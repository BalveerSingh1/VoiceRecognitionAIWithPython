from tkinter import *
from tkinter import messagebox
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' 
Screen=Tk()
Screen.title("Registration Form")
Screen.geometry("500x500")
Screen.resizable(False,False)

def Register():
    Name=NameInfo.get()
    GetName=User_Name(Name)                                             
    inputAge=AgeInfo.get()
    Input_Age=Input_age(inputAge)
    
    Phone=PhoneNOInfo.get()
    PhoneNo=Phone_No(Phone)
    Email=EmailInfo.get()
    YourEmail=User_Email(Email)
    # if(GetName==True and InputAge==True and PhoneNo==True and YourEmail==True  ):
    if(True):
        with open(GetName+".txt","w")as f:
           f.write("Name:- "+GetName+"\n")
           f.write("Age:- "+Input_Age+"\n")
           f.write("Phone:- "+PhoneNo+"\n")
           f.write("Email:- "+YourEmail+"\n")
        p=Label(Screen,text="Registration Sucessful",font="2",fg="green").place(x=300,y=40)

def User_Name(UserName):
    length=len(UserName)
    if(length>0 and length<=120):                
            return UserName
    else: 
        Label(Screen,text="Invalid Name",font="2",fg="red").place(x=370,y=40)
        messagebox.showerror("Error","Please enter your Name")
                  
    
def Phone_No(length): 
    CheckLength=len(length)
    if(CheckLength==10):
        UserPhone=str("+91-"+length)
        return UserPhone
    else:
        Label(Screen,text="Invalid  Number",font="2",fg="red").place(x=360,y=40)              
        return Phone_No(length)
def Input_age(Age):
    if(Age>=10 and Age<=120):
        AgeIntToString=str(Age)
        return AgeIntToString
    else:
        Label(Screen,text="Invalid  Age",font="2",fg="red").place(x=370,y=40)
        return Input_age(Age) 
def User_Email(Email):   
	if(re.fullmatch(regex, Email)):
		return Email
	else:
            Label(Screen,text="Invalid  Email",font="2",fg="red").place(x=370,y=40)
            # messagebox.showerror("Error","Please enter your Email")
            return User_Email(Email)
def Clear():
    NameEntry.delete(0, END)
    AgeEntry.delete(0, END)
    PhoneNOEntry.delete(0, END)
    EmailEntry.delete(0, END)
    
  
# label 
Label(Screen,text="Registration From",font="ariel 20 bold",bg="red",fg="black",).pack(fill="both")
Label(Screen,text="Name",font="20").place(x=35,y=70)
Label(Screen,text="Age",font="20").place(x=35,y=120)
Label(Screen,text="Phone No",font="20").place(x=35,y=170)
Label(Screen,text="Email Id",font="20").place(x=35,y=220)

# input 
NameInfo=StringVar()
AgeInfo=IntVar()
PhoneNOInfo=StringVar()
EmailInfo=StringVar()

NameEntry=Entry(Screen,font="10",bd="4",textvariable=NameInfo)
NameEntry.place(x=140,y=70)
AgeEntry=Entry(Screen,font="10",bd="4",textvariable=AgeInfo)
AgeEntry.place(x=140,y=120)
PhoneNOEntry=Entry(Screen,font="10",bd="4",textvariable=PhoneNOInfo)
PhoneNOEntry.place(x=140,y=170)
EmailEntry=Entry(Screen,font="10",bd="4",textvariable=EmailInfo)
EmailEntry.place(x=140,y=220)
Button(Screen,text="Register",font="20",command=Register).place(x=185,y=290)
Button(Screen,text="Clear",font="20",command=Clear).place(x=325,y=290)

mainloop()

































