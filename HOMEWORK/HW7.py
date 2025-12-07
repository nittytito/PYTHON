inventory =[]
def add_item(item):
    inventory.append(item)
def count_item(item):
    if not item:
        return 0
    return 1 + count_item(item[1:])
display = lambda item: print(f"Item: {item}")
def main():
    add_item("dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")
    print("Pet store inventory")
    for item in inventory:
        display(item)
    total = count_item(inventory)
    print("Total number of items in store:",total)
main()