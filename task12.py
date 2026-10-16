name = input("Employee's name: ")
daily_wage = float(input("Daily wage: "))

present = 0
absent = 0

for day in range(1, 27):
    entry = input("Day " + str(day) + " (P/A): ").upper()
    while entry != "P" and entry != "A":
        print("Invalid! Sirf P ya A likhain.")
        entry = input("Day " + str(day) + " (P/A): ").upper()

    if entry == "P":
        present = present + 1
    else:
        absent = absent + 1

percentage = present / 26 * 100
salary = present * daily_wage

print("Employee:", name)
print("Present days:", present)
print("Absent days:", absent)
print("Attendance:", round(percentage, 2), "%")
print("Salary: Rs.", salary)
if percentage < 80:
    print("WARNING: Attendance below 80%!")