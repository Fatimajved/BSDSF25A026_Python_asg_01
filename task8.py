name = input("Student's naam: ")
book = input("Book's title: ")

days_late = int(input("Days late: "))
while days_late < 0:
    print("Invalid! Days late cannot be negative.")
    days_late = int(input("Enter days late again: "))

if days_late <= 0:
    fine = 0
elif days_late <= 5:
    fine = days_late * 10
elif days_late <= 10:
    fine = 50 + (days_late - 5) * 20
else:
    fine = 150 + (days_late - 10) * 50

print("Book title:", book)
print("Days late:", days_late)
if fine == 0:
    print("No fine is due.")
else:
    print("Total fine: Rs.", fine)