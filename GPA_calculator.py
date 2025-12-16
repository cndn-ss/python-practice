def calculate_gpa(marks):
    total = sum(marks)
    count = len(marks)
    if count == 0:
        return 0
    return total / count

my_marks = [90, 80, 85, 70]
average = calculate_gpa(my_marks)
print(f"My GPA is: {average}")