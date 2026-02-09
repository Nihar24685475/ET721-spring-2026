
import random
import math

def area_rectangle(width,length):
    return width*length

def print_area_result(width,length,area):
    print(f"The area of rectangele of {width} and {length} is {area}")


print("\n------- Example 2: calculate the distance of two points")
#distance = squre_root of ((x2-x1)2 + (y2-y1)2)
#function 1) collect a number between 1 and 10
def collectnum(point):
    num = int(input("enter the  number for {point}: "))
    while(num<1 or num>10):
        num=int(input("Invalid! Enter a numbr between 1 and 10:"))
    return num

def calculate_distance(x1,x2,y1,y2):
    return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

def print_distance(x1,x2,y1,y2,distance):
    print(f"the distance of point ({x1},{y1}) and ({x2},{y2}) is {round(distance)})")

    ##Exercise

def generate_random(min_num, max_num):
    return random.randint(min_num, max_num)

def compare_guess(random_number, user_guess):
    if random_number < user_guess:
        print("The number is smaller than the guess number")
        return False
    elif random_number > user_guess:
        print("The number is bigger than the guess number")
        return False
    else:
        print("You got it!")
        return True