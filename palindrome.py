word=input("Enter the word:")

#rev is variable
rev=word[::-1] 

if(rev==word):
    print( word,"is palindrome")
else:
    print(word," is not palindrome")
