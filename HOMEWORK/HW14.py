import random
import math
name_input = input("Enter customer names: ")
name_list = [name.strip() for name in name_input.split(",")]
unique_name = list(set(name_list))
random.shuffle(unique_name)
win = random.sample(unique_name, 2)
win1 = win[0][::-1]
win2 = win[1][::-1]
total_participant = len(unique_name)
round_sqrt = round(math.sqrt(total_participant))
print("\nLucky Draw Winners")
print("Winner 1 :", win1)
print("Winner 2 :", win2)
print("Total Unique Participants:", total_participant)
print("Rounded Square Root of Participants:", round_sqrt)
