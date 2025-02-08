import os
import tempfile
import platform
import shutil

file_path = os.path.join(os.getcwd(), "abhiraj_example2.txt") #Create a path and dissect it into directory and file name
directory, file_name = os.path.split(file_path)
print(f"Full Path: {file_path}")
print(f"Directory: {directory}")
print(f"File Name: {file_name}")

def list_directory_contents(path="."): #Listing directory contents
    print("\nDirectory Contents:")
    for item in os.listdir(path):
        print(item)

list_directory_contents()

dir_name = "Sample_Directory" #Create a directory called `Sample_Directory`
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"\nDirectory '{dir_name}' created.")

def remove_file_or_directory(path): #Remove files and directories
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' deleted.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory '{path}' deleted.")
    else:
        print(f"'{path}' does not exist.")

print("\nExecuting shell command:") #Executing a shell command `Hello World`
os.system('Hello World')

print("\nEnvironment Variables:") #Extracting and printing environment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")

#Change the current working directory
new_dir = os.getcwd()  # Keeping track of original directory
try:
    os.chdir(dir_name)
    print(f"\nChanged working directory to: {os.getcwd()}")
    os.chdir(new_dir)  # Changing back to original directory
except Exception as e:
    print(f"Error changing directory: {e}")

def check_path(path): #Checking whether a directory or file exists and determine its type
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"'{path}' is a file.")
        elif os.path.isdir(path):
            print(f"'{path}' is a directory.")
    else:
        print(f"'{path}' does not exist.")

check_path(dir_name)
check_path(file_path)

with tempfile.TemporaryFile() as temp_file: #Create a temporary file and directory
    print("\nTemporary file created:", temp_file.name)

with tempfile.TemporaryDirectory() as temp_dir:
    print("Temporary directory created:", temp_dir)

print("\nSystem Information:") #Getting system information
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")

# remove_file_or_directory(dir_name)
