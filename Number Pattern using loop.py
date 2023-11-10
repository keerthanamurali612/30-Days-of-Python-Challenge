# Prompt the user to enter the number of rows for the pattern
num=int(input("Enter the rows:"))

# Outer loop to iterate through each row
for i in range(1,num+1):
    
    # Inner loop to iterate through each column in the current row
    for j in range(1,i+1):
        
        # Print the current column number without moving to the next line
        print(j,end="")

         # Move to the next line after printing all columns in the current row
    print("\n")    
