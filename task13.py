rows = int(input("Rows: "))
while rows < 0:
    print("Invalid!")
    rows = int(input("Enter rows again: "))

seats = int(input("seats on each row: "))
while seats < 0:
    print("Invalid!")
    seats = int(input("Enter seats again: "))

capacity = rows * seats

seat_number = 1
for r in range(rows):
    for s in range(seats):
        print(seat_number, end="\t")
        seat_number = seat_number + 1
    print()

print("Total capacity:", capacity)

customers = int(input("Number of customers: "))
while customers < 0 or customers > capacity:
    print("Invalid! Please enter a number between 0 and", capacity)
    customers = int(input("Enter the number of customers again: "))

print("Unoccupied seats:", capacity - customers)