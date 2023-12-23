# Q3.  .Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis.


import numpy as np

ft_emp = np.array([[101, 'John Doe', 'Full-Time', 55000],
                   [102, 'Jane Smith', 'Full-Time', 60000],
                   [103, 'Mike Johnson', 'Full-Time', 52000]])

pt_emp = np.array([[201, 'Alice Brown', 'Part-Time', 25000],
                   [202, 'Bob Wilson', 'Part-Time', 28000],
                   [203, 'Emily Davis', 'Part-Time', 22000]])

dataset = np.concatenate((ft_emp, pt_emp), axis=0)
print("Combined Employee Data: ")
for i in dataset:
    print("Employee ID: " + str(i[0]) + ", Name: " + str(i[1]) + ", Type: " + str(i[2]) + ", Salary: " + str(i[3]))

