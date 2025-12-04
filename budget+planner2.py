print("\n-----MONTHLY PLANNER-----\n")

income = int(input("Enter Income: "))
rent = int(input("Enter Rent: "))
groceries_expense = int(input("Enter Groceries expense: "))
internet = int(input("Enter Internet : "))
others = int(input("Enter Others: "))

total_expense = rent + groceries_expense + internet + others
savings = income - total_expense

print("-------------------")
print(f"TOTAL INCOME: ₹{income}")
print(f"TOTAL EXPENSE: ₹{total_expense}")
print("--------------------")
print(f"TOTAL SAVINGS: ₹{savings}")
print("--------------------")