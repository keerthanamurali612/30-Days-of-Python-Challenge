year=int(input("Enter the year of services:"))
salary=int(input("Enter the your salary:"))

if year>10:
    bonus=salary*10/100
    print("the net bonus of 10% amount is:","Rs.",int(bonus),"per month")
elif year>=6 and year<=10:
    bonus=salary*8/100
    print("the net bonus of 8% amount is:","Rs.",int(bonus),"per month")
elif year<6:
    bonus=salary*5/100
    print("the net bonus of  5% amount is:","Rs.",int(bonus),"per month")
else:
    print("invalid")
    
