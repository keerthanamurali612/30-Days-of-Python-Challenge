age=int(input("Enter the age:"))
gender=input("enter the gender:")

if age>=18 and age<30:
    if gender=='m':
        print("wage/day is 700")
    elif gender=='f':
        print("wage/day is 750")

elif age>=30 and age<=40:
    if gender=='m':
        print("wage/day is 800")
    elif gender=='f':
        print("wage/day is 850")
