price = int(input("Enter price: "))
current_saving = 0

while( current_saving < price):
    deposite = int(input("Enter deposite amount: "))
    current_saving = current_saving + deposite
    amount_needed = price - current_saving
    if current_saving < price:
        print(f"You have saved ₹{current_saving:.2f} and need more ₹{amount_needed:.2f} ")
print(f"You saved enough ₹{price:.2f}")