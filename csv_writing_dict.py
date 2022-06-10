import csv

with open('employee_file2.csv', mode = 'w') as employee_file2:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(employee_file2, fieldnames = fieldnames)
    # dictreader와 다르게 fieldnames parameter가 필요함

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyer', 'dept': 'IT', 'birth_month': 'July'})