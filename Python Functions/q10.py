def print_odd_numbers(n): #Prints=ing only odd numbers from 0 to n
    for i in range(n + 1):  #Loop goes till n+1 to include n
        if i % 2 != 0:  
            print(i, end=" ") #Adding space in the end

print_odd_numbers(21)
