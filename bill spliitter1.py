person = int(input("Enter number of person: "))
total_bill = float(input("Enter total bill: "))
tip = float(input("Enter tip amount: "))

splitted_bill = total_bill / person
tip = tip / person
print(f"Split Bill: ₹{splitted_bill} | Tip Share: ₹{tip}")


