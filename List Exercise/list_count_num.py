#Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

a=[2, 7, 5, 64, 14]
e_count=0
o_count=0
for i in a:
    if(i%2==0):
        e_count=e_count+1
    elif(i%2!=0):
        o_count=o_count+1

print(f"the even number in a list {e_count}")
print(f"the odd number in a list {o_count}")
