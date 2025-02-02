def print_table(): #Takes a number as input and prints its multiplication table till 10
    num = int(input("Enter number: ")) #Input the number
    for i in range(1, 11): #For loop goes till 10
        print(f"{num} x {i} = {num * i}") #Prints the table accordingly

print_table()
