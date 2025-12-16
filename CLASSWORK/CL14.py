import random
import math
name_input = input("Enter the names of invited guests: ")
name_list = [name.strip() for name in name_input.split(",")]
unique_names = list(set(name_list))
select_name = random.choice(unique_names)
reverse_name = select_name[::-1]
count_unique = len(unique_names)
round_sqrt = round(math.sqrt(count_unique))
print("\nBirthday Game")
print("Select Name:", select_name)
print("Reverse Name:", reverse_name)
print("Total Unique Names:", count_unique)
print("Rounded Square Root:", round_sqrt)
