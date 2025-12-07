grocery_list = ["Milk","Bread","Eggs"]
def add_item(item):
    grocery_list.append(item)
def remove_item(item):
        grocery_list.remove(item)
display = lambda item : print(f"Items: {item}")
def character_count(items):
    if not items:
        return 0
    else:
        return len(items[0]) + character_count(items[1:])
add_item("Butter")
add_item("Sugar")
remove_item("Sugar")
for item in grocery_list:
    display(item)
total = character_count(grocery_list)
print("Total characters: ",total)