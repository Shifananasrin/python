
student = {
    "name": "Riya",
    "roll_number": "45",
    "registration_number": "REG20261815",
    "department": "Computer Science",
    "semester": "S2"
}
print("student details",student)
print()
student["total_mark"] = 82 
print()
if student["total_mark"] >= 90:
    student["grade"] = "A"
elif student["total_mark"] >= 82:
    student["grade"] = "B"
elif student["total_mark"] >= 75:
    student["grade"] = "C"
elif student["total_mark"] >= 60:
    student["grade"] = "D"
elif student["total_mark"] >= 50:
    student["grade"] = "P"
else:
    student["grade"] = "F"
print(student)
print()
del student["roll_number"]

print(student)
