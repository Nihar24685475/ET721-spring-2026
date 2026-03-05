"""
Nihar patel
March 3, 2026
lab 10, unit testing using pytest
"""

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

# #local testing x
print(add(2,3))#5
print(add(-8,5))# -3
print(subtract (7,5))# 2
print(subtract(-7,5)) #-12
print(subtract(-7,-5))#-2

#lab exercise 1 : basic testing
def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

# #local testing
# print(divide(5,2)) # 2.5
# print(divide(3,0)) # error

#lab exercise 2 : password validation: 8+ characters, at least 1 uppercase, 1 lowercase, 1 digit
def validate_password(password):
    password = password.strip() # remove leading and ending whitespace
    special_characters = "%" in password or '#' in password or ' ' in password
    if len(password) < 8 or special_characters:
        return False
    return True

# local testing
print(validate_password("peterpan")) 
print(validate_password("peter pan")) 
print(validate_password("peter#pan")) 
print(validate_password("peter%pan")) 
print(validate_password("peter$pan")) 
print(validate_password("pan"))

#lab exercise 3 : test if a number is even
def is_even(n):
    return n % 2 == 0

#local testing
print(is_even(8))
print(is_even(-5))
print(is_even(0))
print(is_even(-12))
print(is_even(11))