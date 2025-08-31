import csv

employee_file = open("employees.csv")

csv_employee_file = csv.reader(employee_file)

for row in csv_employee_file:
    name, phone, role = row    
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))

employee_file.close()