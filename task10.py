name = input("Customer's name: ")
balance = int(input("Current balance: "))

success_count = 0
total_withdrawn = 0

while True:
    print("1. Withdraw")
    print("2. Exit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "2":
        break
    elif choice == "1":
        amount = int(input("Withdrawal amount: "))

        if amount <= 0:
            print("Failed: Amount must be a positive integer.")
        elif amount % 500 != 0:
            print("Failed: Amount must be a multiple of 500.")
        elif amount > balance:
            print("Failed: Insufficient balance.")
        else:
            balance = balance - amount
            success_count = success_count + 1
            total_withdrawn = total_withdrawn + amount
            print("Success! Rs.", amount, "nikal liye gaye.")
        print("Updated balance: Rs.", balance)
    else:
        print("Failed: Invalid option.")

print("Successful withdrawals:", success_count)
print("Total withdrawn: Rs.", total_withdrawn)
print("Final balance: Rs.", balance)