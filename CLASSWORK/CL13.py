statinery_items = input("Enter the name of new item:").strip()
filename = "items.txt"

try:
    with open(filename,"a") as file:
        file.write(statinery_items + "\n")
    print("\n Item added successfully")
except Exception as e:
    print("\nError",e)
try:
    print("\nFull list of items")
    with open(filename,"r") as file:
        for line in file:
            print("",line.strip())
except Exception as e:
    print("\nError",e)