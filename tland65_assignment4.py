import csv
import statistics

student_name = 'Todd Landry Jr'

avg_city = [0]
avg_hwy = [0]
ford_hwy = [0]
suv_city = [0]

with open('mpg.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        return row

