"""
niahr patel
Feb3 ,2026

"""
print("\n --- example ! : set-up of conditional statement---")
#conditional statment states the flow thee program
age =11
if(age>=21):
    print("you are an adult!")
elif(age<21 and age >= 12):
    print("you are a teen")
elif(age<12 and age>0):
    print("you are a kid")
else:
    print("unable to read age")

print("\n --- exmaple 2: for loop-----")
#for loop as a counter to print from 9 to 1 , step 1
for n in range(9,0,-1):
    print(n)
#for loop in list
numbers = [3,6,1,-8,9,-5]
for m in numbers:
    print(m)

#for loop in list 
print ("\n--- exmaple 3:for loop in list----")
numbers =[3,6,1,-8,9,-5]
count_negative = 0
for m in numbers:
    if m<0:
        count_negative += 1
else:
    print(f"There is/are {count_negative}negative numbers")

print('\nEND OF PROGRAM!')
print("\n---- exmaple 4 : while loop as a counter---")
#while loop to print for -3 to 5, inclusive, step of 2, out --> -3 -1 1 3 5

x = -3 
while x <= 5:
    print(x)
    x += 2

print("\n---- example 5: while loop to validate an input -----")
#program collacts a number form user and print if the number is even or odd
#after it, the program will ask the user if another will be tested
#if the user type 'y' or 'Y' then the program will run again
#if the user types any other character that is not 'y' or 'Y',the program will stop

decision_user = 'y'
user_number = 0
while True:
    user_number = int(input("Enter a number: "))
    if user_number%2 == 0 and user_number != 0 :
        print(f"{user_number} is EVEN")
    elif user_number == 0:
        print("The number is zero")
    else:
        print(f"{user_number} is ODD")
    
    decision_user= input ("Do you want another run? Y or y for yes: ")
    if decision_user != 'y' and decision_user != 'Y':
     break

print ("\n -- exercise 1 : use 'while' loop to validate that the 'user_number' is between 1 and 9")

while True: 
    user_Enterednumber = int(input("Enter the number between 1 to 9: "))
    if 1 <= user_Enterednumber <= 9:
        print("valid number")
        break
    else:
        print("try again. enter a number between 1 and 9.")

print ("\n --- exercise 2 : guess the right number , three attempt ----")

number1 = 9
counter = 0
for m in number1:
    if m == number1:
    print("correct guess")
    break
elif:
    Print("try again")
    
