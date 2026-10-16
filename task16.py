child_count = 0
adult_count = 0
senior_count = 0
total_revenue = 0

while True:
  age_input = input("Enter customer's age (or type 'done' to finish): ")
  if age_input.lower() == "done":
    break

  age = int(age_input)
  if age < 0:
    print("Age cannot be negative. Please enter a valid age.")
    continue

  if age < 12:
    price = 300
    child_count += 1
    category = "Child"
  elif 12 <= age <= 59:
    price = 600
    adult_count += 1
    category = "Adult"
  else:
    price = 400
    senior_count += 1
    category = "Senior"

  total_revenue += price
  print(f"Ticket sold for {category} (Age {age}): Rs. {price}")

total_tickets = child_count + adult_count + senior_count

print("\n--- Cinema Ticket Sales Summary Report ---")
print(f"Total Tickets Sold: {total_tickets}")
print(f"  - Child Tickets (<12): {child_count} (Rs. {child_count * 300})")
print(f"  - Adult Tickets (12-59): {adult_count} (Rs. {adult_count * 600})")
print(f"  - Senior Tickets (60+): {senior_count} (Rs. {senior_count * 400})")
print(f"Total Revenue: Rs. {total_revenue}")

if total_tickets > 0:
  avg_price = total_revenue / total_tickets
  print(f"Average Ticket Price: Rs. {avg_price:.2f}")
else:
  print("No tickets were sold.")