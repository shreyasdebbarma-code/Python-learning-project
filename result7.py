name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 70:
    print(f"You passed:")
elif marks <=40:
    print(f"You failed:")
else:
    print("You passe with average score")
print("---------RESULT--------")
print(name)
print(marks)