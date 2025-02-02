def check_odd_even_(num): #Checks if the given number is odd or even by checking divisibility by 2
    if num % 2 == 0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

check_odd_even_(10)  #Output: 10 is Even
check_odd_even_(7)   #Output: 7 is Odd
