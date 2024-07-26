import csv 

name = input("What's your name? ")
home = input("Where's your home? ")

with open("student.csv", 'a') as file:
    # we use dictwriter here because we want to write a dictionary to the file
    # csv.DictWriter is a class that makes it easy to write tabular data to a file.
    writer = csv.DictWriter(file, fieldnames=['name', 'home']) # we '' for the name of the strings(columns that are in the csv file )
    writer.writerow({'name': name, 'home': home}) # users write the name and home to the file