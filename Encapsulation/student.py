# Write a Python program to create a person class.
# The class should have three private variables: name, age, and gender.
# The class should also have a constructor that takes the name, age, and gender as arguments,
# getter methods for all three variables, and setter methods for the name and age.

class Person:
    def __init__(self,name,age,gender):
        self.__name=name
        self.__age=age
        self.__gender=gender

    def get_Person(self):
       print(f"name name: { self.__name}, age : { self.__age },gender : {self.__gender}")

    def set_Person(self):
        print(f"name : {self.__name}, age :{self.__age}")

person1=Person("rudra",24,"female")
person1.set_Person()
