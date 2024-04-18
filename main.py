 # Global variable that stores the name of the file
file_name = "data.txt"

# Function to clear the file
def clear_file():
    with open(file_name, 'w') as file:
        pass

# Function to write data to the file
def write_data(data):
    with open(file_name, 'w') as file:
        file.write(data)

# Function to read data from the file
def read_data():
    with open(file_name, 'r') as file:
        data = file.read()
    return data

# Clear the file
clear_file()

# Write "hello how are you" to the file
write_data("hello how are you\n")

# Read and print the data from the file
print(read_data())
