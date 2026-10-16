name = input("Enter your name :")
grand_total = 0;
more = "y"

while more == "y" or more == "Y":
    print ("1.Sandwich    Rs. 250")
    print("2.Burger       Rs. 400")
    print("3.Pizza slice  Rs. 300")
    print("4.Juice        Rs. 120")

    choice = int(input ("Select item number"))
    if choice < 1 or choice > 4:
        print ("Invalid choice")
    else:
        if choice == 1: 
           item = "Sandwich"
           price = 250
        elif choice == 2:
           item = "Burger"
           price = 400
        elif choice == 3:
           item = "Pizza slice"
           price = 300
        else:
           item = "Juice"
           price = 120 
    quantity = int (input ("Enter Quantity "))
    if quantity <=0:
        print ("Invalid Quantity")
    else:
        subtotal = price * quantity
    
    if subtotal >=1000:
        discount = subtotal* 0.10
    else:
        discount = 0        

    final = subtotal - discount
    grand_total = grand_total + final

    print ("------RECEIPT------")
    print ("Name:", name)
    print ("Item:", item)
    print ("Quantity:" , quantity)
    print ("Subtotal: Rs. " , subtotal)
    print("Discount: Rs.", discount)
    print("Final Bill: Rs.", final)
    print("---------------------")

    more = input("Want to order more? (y/n): ")

print("\nTotal of all orders: Rs.", grand_total)
    
    