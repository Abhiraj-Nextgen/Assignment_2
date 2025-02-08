import os

def read_file(filename): #Read a file
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content): #Write on a file
    with open(filename, 'w') as file:
        file.write(content)

def append_file(filename, content): #Append on a file
    with open(filename, 'a') as file:
        file.write(content)

def read_lines(filename): #Read lines into a list and iterate over each line in a file
    with open(filename, 'r') as file:
        lines = file.readlines()
    for l in lines:
        print(l.strip())

def file_exists(filename): #Check if the file exists
    return os.path.exists(filename)

def write_list_to_file(filename, lines): #Write a list into a file
    with open(filename, 'w') as file:
        file.writelines(f"{line}\n" for line in lines)

def process_multiple_files(file1, file2): #Use `with` keyword for multiple files
    with open(file1, 'r') as f1, open(file2, 'w') as f2:
        f2.write(f1.read())

def delete_file(filename): #Delete a file
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted.")
    else:
        print(f"{filename} does not exist.")

def copy_binary_file(source, destination): #Read and write binary files
    with open(source, 'rb') as src, open(destination, 'wb') as dest:
        dest.write(src.read())

filename = "abhiraj_example.txt"

write_file(filename, "Writing to a file.\n")

append_file(filename, "Appending another line.\n")

print("File Content:")
print(read_file(filename)) #Reading a file

print("\nReading lines into a list and iterating:")
read_lines(filename)

print("\nChecking if file exists:", file_exists(filename))

write_list_to_file(filename, ["Line 1", "Line 2", "Line 3"]) #Writing list to file

print("\nAfter writing list to file:")
print(read_file(filename))

#Copy binary file (example with a binary file)
binary_src = "source.bin"
binary_dest = "copy.bin"
write_file(binary_src, "Binary content")  #Creating a dummy binary file
copy_binary_file(binary_src, binary_dest)


delete_file(filename) #Deleting the files
delete_file(binary_src)
delete_file(binary_dest)
