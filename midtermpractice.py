print("Employee Salary and Bonus Calculator")
print("-" * 40)

num_employees = int(input("Enter number of employees: "))
emp_count = 1

while emp_count <= num_employees:
    print("\nEmployee", emp_count)
    name = input("Enter employee name: ")
    base_salary = float(input("Enter base salary: "))
    total_hours = 0
    days = int(input("Enter number of working days: "))

    for d in range(1, days + 1):
            hours = int(input("Enter hours worked on day " + str(d) + ": "))
            total_hours += hours

    avg_hours = total_hours / days

    if avg_hours >= 9:
        bonus = base_salary * 0.20
    elif avg_hours >= 7:
        bonus = base_salary * 0.10
    else:
        bonus = 0

    final_salary = base_salary + bonus

    print("\nReport for:", name)
    print("Base Salary:", base_salary)
    print("Average Hours:", avg_hours)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)
    print("-" * 40)

    emp_count += 1

print("\nAll employees processed. Program ended.")

print("Student Attendance Tracker")
print("-" * 40)

# Number of students
num_student = int(input("Enter number of students: "))

# Counter for while loop
count = 1

# While loop for each student
while count <= num_student:     # (1) loop until all students are processed
    print("\nStudent", count)
    name = input("Enter student name: ")

    total_days = int(input("Enter total working days: "))
    present_days = 0

    # For loop to record attendance
    for d in range(1, total_days + 1):    # (2) loop through working days
        status = input("Was student present on day " + str(d) + " (y/n)? ")
        if status == "y":
            present_days += 1   # (3) count as present

    # Calculate attendance percentage
    percentage = (present_days / total_days) * 100   # (4) calculate %

    # Determine eligibility using if-elif-else
    if percentage >= 90:
        status = "Excellent Attendance"
    elif percentage >= 75:
        status = "Good Attendance"
    elif percentage >= 50:
        status = "Needs Improvement"
    else:
        status = "Poor Attendance"   # (5) Poor Attendance

    # Display report
    print("\nReport for:", name)
    print("Total Days:", total_days)
    print("Present Days:", present_days)
    print("Attendance %:", percentage)   # (6) print percentage
    print("Status:", status)

    print("-" * 40)

    # Increase student counter
    count += 1   # (7) move to next student

print("\nAll students processed. Program ended.")   # (8) program ends message


print("Electricity Bill Calculator")
print("-" * 40)

# Number of customers
num_customers = int(input("Enter number of customers: "))

# Counter for while loop
count = 1

# While loop for each customer
while count <= num_customers:   # (1) loop for all customers
    print("\nCustomer", count)
    name = input("Enter customer name: ")
    units = int(input("Enter number of units consumed: "))

    bill = 0

    # For loop to calculate charges for each slab
    for u in range(1, units + 1):
        if u <= 100:
            bill += 5  # (2) charge per unit for first 100 units
        elif u <= 200:
            bill += 7  # (3) charge per unit for next 100 units
        else:
            bill += 9   # (4) charge per unit beyond 200 units

    # Apply surcharge if bill exceeds 3000
    if bill > 3000:   # (5) threshold
        bill += bill * 0.05   # 5% surcharge

    # Display customer bill
    print("\nBill for:", name)
    print("Units Consumed:", units)
    print("Total Bill Amount:", bill)   # (6) print bill

    print("-" * 40)

    # Move to next customer
    count += 1   # (7) increment counter

print("\nAll customers processed. Program ended.")   # (8) program ends message


print("Student Marks and Grade Calculator")
print("-" * 40)

# Number of students
num_students = int(input("Enter number of students: "))
count = 1   # (1) student counter

# While loop for each student
while count <= num_students:   # (2) loop condition
    print("\nStudent", count)   # (3) student number
    name = input("Enter student name: ")

    total_marks = 0
    num_subjects = int(input("Enter number of subjects: "))
    sub_count = 1   # (4) subject counter

    # While loop to enter marks for each subject
    while sub_count <= num_subjects:   # (5) loop condition
        mark = int(input("Enter mark for subject " + str(sub_count) + ": "))   # (6) subject number
        total_marks += mark   # (7) add mark to total
        sub_count += 1   # (8) increment subject counter

    # Calculate average
    average = total_marks / num_subjects   # (9) total / number of subjects

    # Determine grade using if-elif-else
    if average >= 90:   # (10) check for A
        grade = "A"
    elif average >= 75:   # (11) check for B
        grade = "B"
    elif average >= 50:   # (12) check for C
        grade = "C"
    else:
        grade = "F"   # (13) failing grade

    # Display result
    print("\nReport for:", name)   # (14) student name
    print("Total Marks:", total_marks)    # (15) total marks
    print("Average Marks:", average)  # (16) average
    print("Grade:", grade)          # (17) grade

    print("-" * 40)

    count += 1   # (18) increment student counter

print("\nAll students processed. Program ended.")   # (19) program ends message