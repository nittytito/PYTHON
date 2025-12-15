filename = "students.txt"
try:
    with open(filename, "r") as f:
        print("Existing names:")
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("File not found. New file will be created.")
n = int(input("How many names? "))
with open(filename, "a") as f:
    for i in range(n):
        f.write(input("Enter name: ") + "\n")
print("\nUpdated names:")
with open(filename, "r") as f:
    for line in f:
        print(line.strip())
