import numpy as np

arr = np.array([1, 2, 3, 4, 5]) #Creating a numpy array

#Creating an array of zeros and ones
zeros_arr = np.zeros((3, 3))  # 3x3 matrix of zeros
ones_arr = np.ones((3, 3))    # 3x3 matrix of ones

#Creating a sequence of range using numpy inbuilt function
range_arr = np.arange(10, 50, 5)  #Starts at 10, ends before 50, step of 5

#Creating a series of values evenly distributed between two bounds
linspace_arr = np.linspace(1, 10, 5)  #5 values between 1 and 10

#Reshaping the array
reshaped_arr = np.arange(1, 10).reshape(3, 3)  # 3x3 matrix

#Showcasing the use of operators on arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr = arr1 + arr2  #Element-wise addition
mul_arr = arr1 * arr2  #Element-wise multiplication

#Performing all sorts of matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(matrix1, matrix2)  #Dot product
element_wise_mult = matrix1 * matrix2  #Element-wise multiplication

#Access array elements
one_d_element = arr[2]  #Accessing 3rd element of 1D array
multi_d_element = reshaped_arr[1, 2]  #Accessing element at row 1, column 2

#Filtering based on conditions
filtered_arr = arr[arr > 2]  #Getting all elements greater than 2

#Using statistical functions
mean_value = np.mean(arr)  #Mean
std_dev = np.std(arr)  #Standard deviation
max_value = np.max(arr)  #Maximum value
min_value = np.min(arr)  #Minimum value

print("a. Numpy Array:\n", arr)
print("b. Zeros Array:\n", zeros_arr)
print("b. Ones Array:\n", ones_arr)
print("c. Range Array:\n", range_arr)
print("d. Linspace Array:\n", linspace_arr)
print("e. Reshaped Array:\n", reshaped_arr)
print("f. Sum of Arrays:\n", sum_arr)
print("f. Multiplication of Arrays:\n", mul_arr)
print("g. Dot Product:\n", dot_product)
print("g. Element-wise Multiplication:\n", element_wise_mult)
print("h. One Dimensional Element:\n", one_d_element)
print("h. Multi Dimensional Element:\n", multi_d_element)
print("i. Filtered Array:\n", filtered_arr)
print("j. Mean:", mean_value)
print("j. Standard Deviation:", std_dev)
print("j. Max Value:", max_value)
print("j. Min Value:", min_value)
