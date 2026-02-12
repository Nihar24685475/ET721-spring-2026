"""
Nihar patel
lab 6, classes , oject , and methods
feb 10, 2026
"""

#import mathplotlib.pylot as plt

print("\n--- example 1: classes")
# a class is like a blueprint of something
#using the class, we can create different intance of an object
#methods are functions of an object

class Circle(object):
    def __init__(self , radius, color):
        self.r=radius 
        self.c=color
        # method to add value to the radius

    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r
        
        
class Rectangle(object):
    def __init__(self ,height,width, color):
        self.h= height
        self.w= width
        self.c= color


    # method to calculate and return the area of the rectangle
    def area(self):
        return  self.h * self.w
    # method to calculate the perimenter of aa rectangle
    def perimeter(self):
        return 2*self.w + 2*self.h
    
    # mehtod to draw the rectangle
def drawRectangle(self):
    plt.gca().add_patch (plt.Rectangle((0,0), self.w,self.h,fc=self.c))
    plt.axis("scaled")
    plt.show()
                  
#creat an instace of an object
circle1 = Circle(5,"yellow")
circle2 = Circle(2, "red")

rectangle1 = Rectangle(2,3,"green")
rectangle2 = Rectangle(5,3,"blue")

print(f"color of circle 2 = {circle2.c}")
print (f"the area of rectangle 1 = {rectangle1.w * rectangle2.h} ")
print (f"the area of rectangle 2 = {rectangle2.w * rectangle1.h} ")

#modify data of an object

circle2.c = "orange"
print(f"color of circle 2 after modification = {circle2.c}")

print(f"radius of circle 2 = {circle2.r}")

#call mehtod add_radius and pass 6
circle2.add_radius(6)
print(f"radius of circle 2 after method add_radius = {circle2.r}")


#call methods in class rectangle 
print(f"The area of rectangle 1 = {rectangle1.area()}")
print(f"The perimeter of rectangle 2 = {rectangle2.perimeter()}")

#draw rectangle
#rectangle2.drawRectangle()

print("\n =------ exercise------")

class BankAccount:
    
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance_amount = 250.50   

    def deposit(self, amount):
        self.balance_amount += amount
        print(f"Deposited ${amount:.2f}")
    
    def withdraw(self, amount):
        if amount <= self.balance_amount:
            self.balance_amount -= amount
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Withdrawal cannot be made. Insufficient balance.")
    
    def balance(self):
        print(f"Final balance $ {self.balance_amount:.2f}")


useraccount = BankAccount(123456789, "Student's name")

useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)
useraccount.balance()
