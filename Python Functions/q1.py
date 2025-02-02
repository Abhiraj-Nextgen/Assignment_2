def hello_without_parameters(): #Takes input and prints hello <name>
    name = input("Enter your name: ")
    print(f"Hello {name}!")

hello_without_parameters()

def hello_with_parameters(name): #Prints hello <name> using a passed parameter <name>
    print(f"Hello {name}!")

hello_with_parameters("Abhiraj")
