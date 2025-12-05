total_bill = 0
order_status = "YES"
while order_status == "YES":
    print("COFFEE : ₹100")
    print("TEA : ₹50")
    print("COOKIES : ₹60")
    item = input("What would you like to order? ").upper()
    if item == "COFFEE":
        total_bill += 100
        print("COFFEE ADDED")
    elif item == "TEA":
        total_bill += 50
        print("TEA ADDED")
    elif item == "COOKIES":
        total_bill += 60
        print("COOKIES ADDED")
    else:
        print("We Dont Serve That")
    order_status = input("Do you want to Another item (YES/NO)? ").upper()
print(f"Your Total Bill is: {total_bill}")
print("Thank You visit Again")