
days = int(input("Enter how many days will be monitored: "))

if days <= 0:
  print("Invalid number of days. Please enter a positive number.")
else:
  total_temp = 0
  highest = None
  lowest = None
  above_35 = 0
  below_10 = 0
  between_10_35 = 0

  for i in range(1, days + 1):
    temp = float(input(f"Enter temperature for day {i} (°C): "))

   
    total_temp += temp
    if highest is None or temp > highest:
      highest = temp
    if lowest is None or temp < lowest:
      lowest = temp

    
    if temp > 35:
      above_35 += 1
    elif temp < 10:
      below_10 += 1
    else:
      between_10_35 += 1

  average = total_temp / days

  print("\n--- Temperature Report ---")
  print(f"Total Days Monitored: {days}")
  print(f"Average Temperature: {average:.2f}°C")
  print(f"Highest Temperature: {highest}°C")
  print(f"Lowest Temperature: {lowest}°C")
  print(f"Days above 35°C: {above_35}")
  print(f"Days below 10°C: {below_10}")
  print(f"Days between 10°C and 35°C (inclusive): {between_10_35}")