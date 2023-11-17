mp=int(input("Enter the marked price:"))

if mp>10000:
    na=mp-20/100
    print("the net amount 20% is:",na)
elif mp>7000 and mp<=10000:
    na=mp-15/100
    print("the net amount 15% is:",na)
elif mp<=7000:
    na=mp-10/100
    print("the net amount 10% is:",na)
else:
    print("invalid")
