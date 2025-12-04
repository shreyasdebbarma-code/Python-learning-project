height = int(input("Height: "))

if height >=120:
    print("You can go")
    age = int(input("Age: "))
    if age >=18:
        print(F"pay ₹100")
    elif age <= 18:
        print("pay ₹50")
elif height < 120:
    print("You can not go: ")
