def swap_numbers(a, b): #Swaping two numbers without using a third variable
    print(f"Initially: a = {a}, b = {b}")
    a = a + b  #First, a becomes sum of a and b
    b = a - b  #Then, b gets original value of a
    a = a - b  #Finally, a gets original value of b

    print(f"After Swapping: a = {a}, b = {b}")
    return a, b  

swap_numbers(10, 20)
