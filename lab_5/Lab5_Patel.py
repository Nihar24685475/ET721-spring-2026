"""
Nihar patel
fab 5, 2026
ET 721
Lab 5

"""
import math
from lab5_function_patel import *
print("\n------- Example 1: user-define function")
w=10
length = 2
a = area_rectangle(w,length)
print_area_result(w,length,a)

print("\n------- Example 2:calculate")
x1= collectnum('x1')
x2= collectnum('x2')
y1= collectnum('y1')
y2= collectnum('y2')

#print(f"({x1},{y1}) ({x2},{y2})")

#print(f"distance={calculate_distance(x1,x2,y1,y2)}")

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2,distance)

print ('\n Exercise')