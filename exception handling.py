filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        contents = file.read()
        print("\nFile Contents:\n")
        print(contents)

except FileNotFoundError:
    print(f"\nError: The file '{filename}' does not exist.")
