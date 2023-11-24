class calculator:
    def __init__(self,a,b):
        self.num1=a #num1 is variable
        self.num2=b #num2 is variable
        
    def add(self): #add is function
        print("add :",self.num1+self.num2)
    def sub(self): #sub is function
        print("sub :",self.num1-self.num2)
    def mul(self): #mul is function
        print("mul :",self.num1*self.num2)
    def div(self): #div is function
        print("div :",self.num1/self.num2)
        
cal=calculator(10,15) #create a obj as a cal
cal.add()
cal.sub()
cal.mul()
cal.div()
