def generate_2d_list(rows, cols): #Generates a 2D list where a[i][j] = i + j
    matrix = []  #Initializing an empty list
    for i in range(rows):  
        row = []  #Creating an empty row
        for j in range(cols):  #Loop through each column
            row.append(i + j)  #Append i+j here
        matrix.append(row)  #Append the row to the matrix

    return matrix 

rows, cols = 4,5
ans = generate_2d_list(rows, cols)

for row in ans:
    print(row)
