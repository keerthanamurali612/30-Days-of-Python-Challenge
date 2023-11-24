'''
Create a class called Car with the following attributes: make, model, year, and color.
 Create a method called drive() that prints a message to the console saying that the car is driving.
 Create an instance of the Car class and call the drive() method
'''
class Car:
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
    def drive(self):
        print("Car_Model:",self.model,
              "Car_Year:",self.year,
              "Car_Color:",self.color
              )
car1=Car("Audi",1997,"White")
car2=Car("BMW",1996,"Black")
car1.drive()
car2.drive()
