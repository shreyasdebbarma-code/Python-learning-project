item = input("Enter item: ")
item_price = float(input("Enter price: "))
discount = float(input("Enter discount: "))

savings = item_price * discount / 100
total_price = item_price - savings

print("\n--- RECEIPT ---")
print("******************************")
print(f"Your item: {item} costs")
print("******************************")
print(f"₹{item_price:.2f}")
print(f"You have got discount of {discount:.2f}%")
print(f"You saved ₹{savings:.2f}")
print("------------------------------")
print(f"Your total price is ₹{total_price:.2f}")
print("******************************")
print("THANKS FOR THE PURCHASE")

