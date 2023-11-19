first=int(input("Enter First Number :"))
second=int(input("Enter Second Number :"))
opr=input("Enter operator:" )


if  opr=='+':
    print("The addition operator of your answer is :",first+second)
elif opr=='-':
    print("The subraction operator of your Answer is:",first-second)
elif opr=='*':
    print("The multiplication operator of your Answer is:",first*second)
elif opr=='/':
    print("The division operator of your Answer is:",first/second)        
else:
    print("invalid")
