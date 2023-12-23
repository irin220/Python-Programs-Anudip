# Q2. Write a python program and iterate the given tuples


employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

employees = (employee1, employee2, employee3)

print("Employee Records: ")
for i in employees:
    print("\nNAME: ", i[0])
    print("\nEMPLOYEE ID: ", i[1])
    print("\nDEPARTMENT: ", i[2])
    print("\nSALARY: ", i[3])
    print("\n")
