pin = int(input("Enter pin: "))
balance = 10000
if pin == 1067810:
    print("Pin correct:")
    if pin == 1067810:
        balance_withdraw= int(input("TO check balance press1: or to withdraw money press2: "))
        if balance_withdraw== 1:
            print(f"Your balance is ₹{balance:.2f}")
        elif balance_withdraw == 2:
            amount_to_withdraw = int(input("Enter amount to withdraw: "))
            if amount_to_withdraw > balance :
                print("You dont have enough money to withdraw from your account: ")
            else:
                remaining_balance = balance - amount_to_withdraw
                print(f"You have withdrawn ₹{amount_to_withdraw:.2f}")
                print(f"Remaining balance in account: ₹{remaining_balance:.2f}")
elif pin != 1067810:
    print("Card Blocked:")


