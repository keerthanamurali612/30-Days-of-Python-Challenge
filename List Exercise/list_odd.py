#Python program to print odd numbers in a List

list=[12, 14, 95, 3, 73]

# iterating each number in list
for i in list:

    # checking condition
    if(i%2!=0):
        print(i,end=",")