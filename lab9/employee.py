"""
Nihar patel
lab 9, unit testing
Feb 26,2026
"""

class Employee:
    #property
    raise_amt = 1.05

    def __init__(self, firstname,lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary
    
    @property
    def emailemployee(self):
        return f"{self.first}_{self.last}@email.org"
    
    @property
    def fullname(self):
        return "f{self.first}{self.last}"
    
    #method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

#local testing
#create instance of the class
employee1 = Employee("Peter","Pan",80000)
print(f"employee = {employee1.fullname}")
print(f"employee email= {employee1.emailemployee}")
print(f"employee salary= ${employee1.salary} per year")
employee1.apply_raise()
print(f"employee salary after the raise = ${employee1.salary} per year")