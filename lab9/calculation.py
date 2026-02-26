"""
Nihar patel
lab 9, unit testing
Feb 26,2026
"""
def addthreenmumber(n1=0,n2=0,n3=0):
    return n1+n2+n3

def subtracttwonumber(n1=0,n2=0):
    return n1-n2

def multiplythreenumber(n1,n2,n3):
    return n1*n2*n3

def dividetwonumber(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("Error! not can't divide by zero")
    except ValueError:
        print("ERROR! not a numerical value")
    except:
        print("ERROR! can't divide the numbers")
