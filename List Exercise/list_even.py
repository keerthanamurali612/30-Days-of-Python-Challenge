#Given a list of numbers, write a Python program to print all even numbers in the given list.

a=[2,7,5,64,14]

# iterating each number in list
for i in a:

    # checking condition
    if(i%2==0):
        print(i, end=",")