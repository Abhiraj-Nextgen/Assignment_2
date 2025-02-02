def using_sum_function(numbers): #Takes a list of numbers and returns the sum using the built-in sum() function
    return sum(numbers)  #Directly calculates and returns the sum of all numbers

numbers_ = [12, 23, 53, 12, 51]
print(f"Sum using sum() function: {using_sum_function(numbers_)}")

def without_using_sum_function(numbers): #Calculates the sum manually by iterating through the list
    total = 0  #Initializing total sum to 0
    for i in numbers:  #Loop through each number in the list
        total += i  #Adding each number to total
    return total  

numbers = [12, 23, 53, 12, 51]
print(f"Sum without using sum() function: {without_using_sum_function(numbers)}")
