fruits = ["Mango","Banana","Apple"]
vegetables = ["Tomato","Cabbage","Potato"]
beverages = ["Tea","Coffe","Juice"]

fruits.append("Pineapple")
print("\nFruits: \n",fruits)

vegetables.insert(1," Carrot")
print("\nVegetables: \n",vegetables)

del beverages[2]
print("\nDelete: \n", beverages)

inventory = [fruits,vegetables,beverages]
print("\nInventory: \n",inventory)

display_2 = fruits[:2]
print("\nSlicing: \n",display_2)

vegetables_list = vegetables[-1]
print("\nVegetables: \n",vegetables_list)

full_length = [len(items) for items in fruits]
print("\nLength: \n",full_length)

if "water" in beverages:
    print("yes")
else:
    print("No")

final_tuple = fruits[0], vegetables[0], beverages[0]
print("\nTuple: \n",final_tuple)