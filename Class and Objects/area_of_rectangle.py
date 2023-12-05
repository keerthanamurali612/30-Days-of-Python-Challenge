#find the area of rectangle using class and objects

class area_of_rect:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display_info(self):
        return self.length*self.width


# Create an object of the Rectangle class
area1=area_of_rect (5,6)

# Calculate and print the area
result=area1.display_info()

print(f"The area of rectangle is:{result}")
