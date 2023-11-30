''' Create a class called Student that inherits from the Person class.
Add the attribute grade to the Student class.
Create a method called get_grade() that returns the student's grade.
Create an object of the Student class and call the get_grade() method. '''

class person:
    def __init__(self ,name,age):
        self.name=name
        self.age=age
    def display_info (self):
        print(f"Name :{ self.name }, Age : {self.age }")
class student(person):
    def __init__(self,name,age,grade):
        # Call the constructor of the base class (Person)
        super().__init__(name, age)
        self.grade = grade
    def get_grade(self):
        return self.grade

s1=student( name="rudra",age=34, grade="A")
s1.display_info()
s1.get_grade()
print(f"Grade: {s1.get_grade()}")