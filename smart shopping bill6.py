name = input("Enter your name: ").upper()
price = float(input("₹Enter your price: "))
quantity = int(input("Enter your quantity: "))
member = input("If you are a member then YES or if not a member then NO: ").upper()


# Calculate the base total first
total_amount = price * quantity

# Apply the discount logic
if member == "YES":
    print("You are a member")
    # UPDATE the existing total_amount variable
    total_amount = total_amount - 40
elif member == "NO":
    print("You are not a member")
    # No math needed here, total_amount stays the same

print("\n--INVOICE--")
print(f"Product: {name}")
print(f"Price: ₹{price:.2f}")
print(f"Qty: {quantity}")
print(f"Total to Pay: ₹{total_amount:.2f}") # Now this prints the updated price