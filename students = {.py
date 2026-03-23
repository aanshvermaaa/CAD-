students = {
    "Rahul": 85,
    "Priya": 92,
    "Aman": 78,
    "Neha": 88
}

topper = max(students, key=students.get)

avg = sum(students.values()) / len(students)

above_avg = {k: v for k, v in students.items() if v > avg}

print("Topper:", topper)
print("Average:", avg)
print("Above Average Students:", above_avg)