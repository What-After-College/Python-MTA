student = {
    "Name":"Jhon",
    "Status": "Pass",
    "marks":85
}

# print(student.keys())
# print(student.values())
# print(student.items())

student["rank"] = 2

# print(student.keys())
# print(student.values())
# print(student.items())
print(student)

# student["marks"] = 88
student.update({"marks":88})

del student['marks']

print(student)

student.clear()
print(student)