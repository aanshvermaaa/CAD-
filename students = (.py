students = (
    ("Rahul", 20, 85),
    ("Priya", 19, 92),
    ("Aman", 21, 78),
    ("Neha", 22, 88),
    ("Rohit", 20, 95),
    ("Anjali", 21, 67)
)

print("STUDENT RECORDS")
for s in students:
    print("Name:", s[0], "Age:", s[1], "Marks:", s[2])

topper = max(students, key=lambda x: x[2])
print("\nTopper of class:", topper[0], "with marks", topper[2])

lowest = min(students, key=lambda x: x[2])
print("Lowest marks:", lowest[0], lowest[2])

total = 0
for s in students:
    total += s[2]

average = total / len(students)
print("Average marks:", average)

print("\nStudents scoring above average:")
for s in students:
    if s[2] > average:
        print(s[0], "-", s[2])

sorted_students = tuple(sorted(students, key=lambda x: x[2], reverse=True))

print("\nStudents sorted by marks:")
for s in sorted_students:
    print(s)

search = input("\nEnter student name to search: ")

found = False
for s in students:
    if s[0].lower() == search.lower():
        print("Student found:", s)
        found = True

if not found:
    print("Student not found")