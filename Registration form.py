import re
# import phonenumbers
# from phonenumbers import geocoder, carrier
# def Mandatory():
def checkName(check):
     length=len(check)
     if(length >0):
          right=check
          return right
     else:
          check=input("Input is Mandatory. Please Enter Input:  ")
          return checkName(check)
def Input_age(InputAge):

    if(InputAge>=10 and InputAge<=120):
        return InputAge
    else:
        # print("OPPS! Your age is not correct")
        InputAge=int(input("OPPS! Your age is not valid. Please enter valid age: "))
        return Input_age(InputAge)
def Input_gender(InputGender):
    if(InputGender=="M" or InputGender=="F" or InputGender=="Other"):
        return InputGender
    else:
        InputGender=input("OPPS ! Wrong invalid Input. Please enter valid input:   ")
        return Input_gender(InputGender)
    
# def Input_gender(InputGmail):
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
	if(re.fullmatch(regex, email)):
		return email
	else:
            email=input("OPPS Invalid Email. please enter valid Email: ")
            return check(email)
            
def Display(Display_Name,Display_age,Display_Gender,input_contact,Display_email):
    print(f"Name : {Display_Name}\nAge : {Display_age}\nGender : {Display_Gender} \nContact : {input_contact}\nEmail : {Display_email}")
def InputContact(Inter_contact):
     length=len(Inter_contact)
     if(length==10):
        #   IndianCode=str(+91)
          FullNumber=str("+91"+Inter_contact)
          return FullNumber
     else:
          Inter_contact=input("OPPS! Not indian Number PLease enter valid indian number:  ")
          return InputContact(Inter_contact)
def LimitOfstring(Limit):
     LengthOfChar=len(Limit)
     if(LengthOfChar<=4000):
          return Limit
     else:
          limit=input("OPPS! Your string is above of limit. please enter Right Input: ")
          return LimitOfstring(Limit)
     

print("Registration Form")
User_input_name=input("Enter a Name: ")
check_name=checkName(User_input_name)
LimitOfChar=LimitOfstring(check_name)
UserInputName=check_name.capitalize()
UserInputAge=input("Enter  Age: ")
CheckAge=checkName(UserInputAge)
Convertint=int(CheckAge)
User_input_Age=Input_age(Convertint)
UserInputGender=input("Enter  gender M/F/Other: ")
checkGender=checkName(UserInputGender)
User_input_Gender=Input_gender(checkGender)
UserInterContact=input("Enter contact: ")
CheckContact=checkName(UserInterContact)
User_input_contact=InputContact(CheckContact)
email =input("Enter  Email: " )
User_input_Gmail=check(email)
Display(UserInputName,User_input_Age,User_input_Gender,User_input_contact,User_input_Gmail)



