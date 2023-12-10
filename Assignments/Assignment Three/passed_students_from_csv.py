# Read CSV file and print names of passed students
import csv

with open('student_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name, age, grade = row
        if int(grade) >= 60:
            print(name)
