year=int(input("Enter the year:"))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print( year ,"is Leap year")
        else:
            print( year ,"is Non Leap year")
    else:
        print( year ,"is Leap year")
else:
    print( year ,"is Non Leap year")


#different way we used
year=int(input("Enter the year:"))

if(year%400==0):
    print(year ,"is Leap year")
elif(year%4==0 and year%100!=0):
    print(year ,"is Leap year")
else:
    print(year ,"is  Non Leap year")
    
