apple_juice=15.5
orange_juice=20
grape_juice=10.25

total_volume=apple_juice+orange_juice+grape_juice
print("The Total Volume Sold = ",total_volume)

total_int=int(total_volume)
print("Total Volume=",total_int)

total_str=str(total_volume)
print("Total Volume=",total_str+"Liter")

import random
bonus_liters=random.randint(5,10)
TOTAL=total_volume+bonus_liters
print("The Total=",TOTAL)