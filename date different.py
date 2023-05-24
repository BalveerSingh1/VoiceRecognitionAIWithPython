import datetime
from datetime import timedelta
time_str = input("Enter start date dd/ mm/ yyyy: ")
FirstDate=datetime.datetime.strptime(time_str,"%d/%m/%Y") 
time_str = input("Enter last date dd/ mm/ yyyy: ")
LastDate=datetime.datetime.strptime(time_str, "%d/%m/%Y") 
diff= abs((FirstDate - LastDate).days)
d=diff%30.436
year=(diff/(30.436*12))
Year=int(year)
month=(diff-((12*Year)*30.436))
Month=int(month/30.436)
day=int(diff%30.436)
print(f"{Year} Year  {Month} Month    {day} Day")


    































