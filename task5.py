student_name = input("Enter your name: ")
monthly_allowance = float(input("Enter your monthly allowance: "))
food_expenses = float(input("Enter your monthly food expenses: "))
transport_expenses = float(input("Enter your monthly transport expenses: "))
internet_expenses = float(input("Enter your monthly internet expenses: "))
book_expenses = float(input("Enter your monthly book expenses: "))
personal_expenses = float(input("Enter your monthly personal expenses: "))
total_expenses = food_expenses + transport_expenses + internet_expenses + book_expenses + personal_expenses
remaining_balance = monthly_allowance - total_expenses

#printing 
print("Name:", student_name)
print("Monthly Allowance:", monthly_allowance)
print("Total Expenses:", total_expenses)
print("Remaining Balance:", remaining_balance)

if monthly_allowance > 0:
     percentage_spent = (total_expenses / monthly_allowance) * 100  
     print ("Percentage spent" , percentage_spent)

     if percentage_spent > 80:
        print("Warning: You have spent more than 80% of your allowance!")
else:
    print("Percentage Spent: cannot be calculated (allowance must be positive)")

if total_expenses < monthly_allowance:
    print("Financial Position: Within Budget")
    
elif total_expenses == monthly_allowance:
    print("Financial Position: Budget Exhausted")
else:
    print("Financial Position: Overspending")