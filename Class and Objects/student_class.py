#Write a Python class named Student with two attributes: student_id, student_name.
#Add a new attribute: student_class.
#Create a function to display all attributes and their values in the Student class.



class student:
    def __init__( self,student_id,student_name):
        self.student_id=student_id
        self.student_name=student_name

        
    def display(self):
        print(
           "Student ID  :",self.student_id,
           "\nStudent Name:", self.student_name,
           "\nStudent_Class :",self.student_class
           )
#create a object
stu1=student(1,"rudra")

#Add a new attribute
stu1.student_class="A1"

#display all attributes 
stu1.display()

        
