def print_pattern(): #Takes the number of rows from user and prints the decreasing star pattern
    rows = int(input("Enter number of rows: "))  
    for i in range(rows, 0, -1):  #Loop from number of rows down to 1
        print("*" * i)  

print_pattern()
