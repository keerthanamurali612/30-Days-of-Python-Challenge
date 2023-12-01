#Given a list of numbers, write a Python program to count positive and negative numbers in a List.

list_num = [2, -7, 5, -64, -14]

pos_count=0
neg_count=0

for i in list_num:
    if(i>=0):
        pos_count=pos_count+1
    elif(i<=0):
        neg_count=neg_count+1

print(f"the count of postive number in the list {pos_count}")
print(f"the count of postive number in the list {neg_count}")