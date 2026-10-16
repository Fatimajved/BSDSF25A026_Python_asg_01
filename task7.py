name = input("Customer's naam: ")
subtotal = 0
total_items = 0

while True:
    product = input("Product's  naam: ")

    price = float(input("Price: "))
    while price <= 0:
        print("Invalid price!")
        price = float(input("Enter price again: "))

    quantity = int(input("Quantity: "))
    while quantity <= 0:
        print("Invalid quantity!")
        quantity = int(input("Enter quantity again: "))

    subtotal = subtotal + price * quantity
    total_items = total_items + quantity

    more = input("Do you want to add more items? (y/n): ")
    if more.lower() != "y":
        break

if subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount_amount = subtotal * discount_rate / 100
final_bill = subtotal - discount_amount

print("Customer:", name)
print("Total items:", total_items)
print("Subtotal: Rs.", subtotal)
print("Discount rate:", discount_rate, "%")
print("Discount amount: Rs.", discount_amount)
print("Final bill: Rs.", final_bill)