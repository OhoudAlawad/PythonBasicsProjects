#Build a countdown calculator. Write some code that can take two dates as input,
#and then calculate the amount of time between them

from datetime import date
 
def numOfDays(date1, date2):
    return (date2-date1).days
     
# Driver program
date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(numOfDays(date1, date2), "days")
