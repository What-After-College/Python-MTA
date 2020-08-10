# student1 = 10
# student2 = 15
# student3 = 14
# student4 = 13
# student5 = 17
# student6 = 19
# student7 = 20
# print(student1)
# print(student2)
#           0   1   2   3   4   5   6   7  8    9 10
student = [10, 15, 14, 13, 17, 19, 20, 45, 96, 458, 452]

# i=0

# while i<len(student):
#     print("Student", i+1 , '= ', student[i])
#     i += 1
#         range(0, 11, 1)
for i in range(len(student)):
    print("Student", i+1, "=", student[i]) 
