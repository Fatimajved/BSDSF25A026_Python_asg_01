num_employees = int(input("Enter the number of employees: "))

if num_employees <= 0:
  print("Zero or negative employee count. No report to generate.")
else:
  total_shop_sales = 0
  target_count = 0
  highest_sales = None
  highest_employees = []
  employee_records = []

  for i in range(1, num_employees + 1):
    print(f"\nEmployee {i}:")
    name = input("Enter employee's name: ")
    sales = float(input("Enter total sales amount: Rs. "))

    while sales < 0:
      print("Sales cannot be negative. Please enter again.")
      sales = float(input("Enter total sales amount: Rs. "))

    employee_records.append((name, sales))
    total_shop_sales += sales

    if sales >= 10000:
      target_count += 1

    
    if highest_sales is None or sales > highest_sales:
      highest_sales = sales
      highest_employees = [name]
    elif sales == highest_sales:
      highest_employees.append(name)

  average_sales = total_shop_sales / num_employees

  print("\n--- Sales Performance Report ---")
  print("Individual Employee Sales:")
  for name, sales in employee_records:
    print(f"  - {name}: Rs. {sales}")

  print(f"\nTotal Shop Sales: Rs. {total_shop_sales}")
  print(f"Average Sales per Employee: Rs. {average_sales:.2f}")
  print(f"Employees meeting target (>= Rs. 10,000): {target_count}")

  if len(highest_employees) == 1:
    print(
        f"Highest-Performing Employee: {highest_employees[0]} with Rs."
        f" {highest_sales}"
    )
  else:
    names_str = ", ".join(highest_employees)
    print(
        f"Highest Sales are tied between: {names_str} with Rs. {highest_sales}"
        " each."
    )