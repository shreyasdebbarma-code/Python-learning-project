total_marks = 0
subject = 5
num_subject = subject
for subject in range(num_subject):
    marks = float(input(f"Enter marks Between (0 and 100) Subject {subject + 1}: "))
    if marks <0 or marks >100:
        print("INVALID INPUT")
    else:
        total_marks += marks
Average = total_marks / 5
Percentage = total_marks / 500 * 100

final_grade = ""

if Percentage >= 90:
    final_grade = "A"
elif Percentage >= 80:
    final_grade = "B"
elif Percentage >= 70:
    final_grade = "C"
else:
    final_grade = "Fail/Improvement"

print(f"THE FINAL GRADE IS: {final_grade}")
print("THE RESULT IS :\n")
print(f"THE total marks is: {total_marks} out of /500")
print(f"THE PERCENTAGE IS {Percentage}%")
print(f"THE FINAL GRADE IS: {final_grade}")



