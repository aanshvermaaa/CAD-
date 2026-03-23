employees = (
    (101, "Amit", 40000),
    (102, "Sita", 50000),
    (103, "Raj", 45000),
    (104, "Neha", 60000)
)

print("Employee Details")
for emp in employees:
    print(emp)

highest = max(employees, key=lambda x: x[2])
print("\nEmployee with highest salary:", highest)

print("\nSalary after 10% increment")
for emp in employees:
    new_salary = emp[2] * 1.10
    print(emp[1], ":", new_salary)