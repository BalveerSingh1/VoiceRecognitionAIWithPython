import math
import myDeviation
def UserInput():
        # create an empty list 
        langlist = []  
        sum=0 
        add=0
        # enter the number of elements as input  
        num = int(input("Enter number of elements for list : "))
        # running loop till the number of element 
        for i in range(0, num): 
            element = int(input(f"Enter the {i+1} value: "))
            langlist.append(element) # appending  element one by one
            # sum of all element
            sum=sum+element
        # print(langlist)  
        # print(sum)
        # avarage of all element
        avg=sum/num
       # print(avg)
        for i in langlist:
            diff=i-avg
            #langlist.append(diff)
           # print(diff)
            square=diff*diff
           # print(square) 
            add=add+square  
        variance=add/num
       # print(variance)
        deviation=math.sqrt(variance)
        print(f"Deviation= {deviation}")

             

        
myDeviation.UserInput()
    

