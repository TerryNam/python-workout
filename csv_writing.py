import csv

with open('employee_file.csv',mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['Jason Muraz', 'Customer Service', 'April'])
    # csv file date 쓰기/ 왜 한 줄씩 띄워지는지 ??