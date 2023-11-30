#Write a Python function to sum all the numbers in a list.

def sum_of_num():
    # Get the number of elements in the list
    num_elements = int(input("Enter the number of elements in the list: "))

    # Initialize an empty list to store numbers
    a = []

    # Get input from the user and add it to the list
    for i in range(num_elements):
        num = int(input(f"Enter number {i + 1}: "))
        a.append(num)

    # Calculate the sum without using the sum() function
    sum=0
    for i in a:
        sum=sum+i
    print(f"The sum of the numbers in the list is: {sum}")

# Call the function
sum_of_num()


