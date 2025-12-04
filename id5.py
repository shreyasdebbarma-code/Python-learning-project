name = input("Enter your name: ")
DOB = int(input("Enter your DOB: "))
college_name = input("Enter your college name: ")
current_year = int(input("Enter your current year: "))
age = current_year - DOB

print("\n GENERATING ID CARD.... \n ")

print(f"* Name:    {name:<20} *")
print(f"* DOB:     {DOB:<20} *")
print(f"* College: {college_name:<20} *")
print(f"* Year:    {current_year:<20} *")
print(f"* Age:     {age:<20} *")
print("*************************************")
