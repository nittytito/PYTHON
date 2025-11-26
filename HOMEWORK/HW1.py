price_of_rice=45
price_of_sugar=40
price_of_oil=130

quantity_of_rice=3
quantity_of_sugar=2.5
quantity_of_oil=1.8

total_price_of_rice=price_of_rice*quantity_of_rice
total_price_of_sugar=price_of_sugar*quantity_of_sugar
total_price_of_oil=price_of_oil*quantity_of_oil

print("Total=",total_price_of_rice)
print("Total=",total_price_of_sugar)
print("Total=",total_price_of_oil)

Total_all=total_price_of_rice+total_price_of_sugar+total_price_of_oil
print("The Total Bill=",Total_all)

bill_int=int(Total_all)
print("Bill as integer=",bill_int)

bill_str=str(Total_all)
print("Bill as string=",bill_str)

import random
delivery_charge=random.randint(5,10)
total_amount=Total_all+delivery_charge
print("Delivery charge=",delivery_charge)
print("Total Amount=",total_amount)