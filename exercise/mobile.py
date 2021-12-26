print("============Mobile Bazar ========")
print("1. Mi (Rs:20000) 2. Oppo(Rs: 30000) 3. Samsung(Rs: 50000)")
option = int(input("Select option: "))
mi_price = 0
oppo_price = 0
samsung_price = 0
total_quantity = 0
delivery_price = 0
plastic_price = 0
bag_price = 0
git_price = 0
tax_amount = 0

if option == 1:
    quantity = int(input("Enter quantity: "))
    total_quantity += quantity
    mi_price = mi_price + 20000 * quantity

elif option == 2:
    quantity = int(input("Enter quantity: "))
    oppo_price = oppo_price + 30000 * quantity
    total_quantity += quantity

elif option == 3:
    quantity = int(input("Enter quantity: "))
    samsung_price = samsung_price + 50000 * quantity
    total_quantity += quantity
else:
    print("invalid option ")
    exit()

print("1. Home(Rs: 1000) 2. Pickup(free)")
dp = int(input("Enter option: "))

if dp == 1:
    delivery_price += 1000

print("1. Plastic(Rs: 500) 2. Bag(Rs: 1000) 3. Gift Box(Rs:2000)")

packing_option = int(input("Enter option: "))
if packing_option == 1:
    plastic_price += 500
elif packing_option == 2:
    bag_price += 1000
elif packing_option == 3:
    git_price += 2000
else:
    exit()

total_amount = mi_price + samsung_price + oppo_price
print('Location: 1. KTM(13% vat) 2. BTK(free) 3. LPT(free)')
lp = int(input("Enter option: "))

if lp == 1:
    tax_amount += total_amount * 0.13

gt = total_amount + tax_amount + bag_price + plastic_price + git_price + delivery_price
print(f"Total Qt: {total_quantity} Price: {total_amount} GT: {gt}")
