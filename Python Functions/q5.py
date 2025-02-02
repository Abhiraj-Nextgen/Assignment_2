from math import sqrt  #Import sqrt from math

def square_root(): #Takes a number from the user and returns its square root
    num = float(input("Enter a number: "))  
    return sqrt(num)

print(f"Square Root: {square_root()}")
