students = {} 

while True:
    name = input("Enter the name of the student: ")
    sid = input("Enter the SID of the student: ")

    students[sid] = name

    more = input("Do you want to add more students (Y/N)? ")
    if more.upper() == 'N':
        break

print("\nStudents' Details:")
for sid, name in students.items():
    print(f"SID: {sid}, Name: {name}")

sorted_students = sorted(students.items(), key=lambda x: x[1])

print("\nSorted Students (by name):")
for sid, name in sorted_students:
    print(f"SID: {sid}, Name: {name}")

sorted_students = sorted(students.items(), key=lambda x: x[0])

print("\nSorted Students (by SID):")
for sid, name in sorted_students:
    print(f"SID: {sid}, Name: {name}")

sid = input("\nEnter the SID of the student you want to search: ")
if sid in students:
    print(f"Name of the student with SID {sid}: {students[sid]}")
else:
    print(f"No student found with SID {sid}")
