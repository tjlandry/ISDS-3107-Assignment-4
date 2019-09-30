import csv
import numpy as np

student_name = 'Todd Landry Jr'

# Disclaimer: I used some pretty extreme methods to complete
# this assignment. There are much easier methods to index and
# perform these calculations. I used list comprehension solely
# to learn more about it and challenge myself.

# Initialize lists for storing CSV columns
city = []
hwy = []
make = []
classes = []


def ReadCSV():
    # Open CSV file in read mode
    with open('mpg.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Skip header row (first row)
        next(reader)
        # Iterate through each row and append columns to respective lists by their indexes
        for row in reader:
            city.append(int(row[8]))
            hwy.append(int(row[9]))
            make.append(str(row[1]))
            classes.append(str(row[11]))
ReadCSV()


def Calculations():
    # NumPy average function
    avg = np.average

    # Rounded average city MPG for all vehicles
    avg_city = round(avg(city), 2)

    # Rounded average highway MPG for all vehicles
    avg_hwy = round(avg(hwy), 2)

    # Rounded average highway MPG for all Ford vehicles
    fords = []
    ford_index = [i for i,x in enumerate(make) if x == 'ford']
    [fords.append(int(hwy[x])) for x in ford_index]
    ford_hwy = round(avg(fords), 2)
    
    # Rounded average city MPG for all SUVs
    suvs = []
    suv_index = [i for i,x in enumerate(classes) if x == 'suv']
    [suvs.append(int(city[x])) for x in suv_index]
    suv_city = round(avg(suvs), 2)

    # String conversion / return statement / line formatting to be used in WriteOutput()
    return 'Todd Landry Jr -  Assignment 4\n\navg_city:  ' + str(avg_city) + ' mpg\navg_hwy:  ' + str(avg_hwy) + ' mpg\nford_hwy:  ' + str(ford_hwy) + ' mpg\nsuv_city:  ' + str(suv_city) + ' mpg'


def WriteOutput():
    # Call Calculations() to store the returned variables
    output = Calculations()
    # Create text file in write mode
    with open('tland65_assignment4.txt', 'w') as txt_file:
        # Write the output of Calculations() to txt_file
        txt_file.write(output)
WriteOutput()
