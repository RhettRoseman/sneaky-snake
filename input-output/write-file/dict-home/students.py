# import csv to use it in code
import csv
# user prompts 
name = input("What's your name? ")
home = input("Where's your home?")

# with statement
# a = append
with open("students.csv", "a") as file:
    writer = csv.writer(file) # we want to write to file we use csv writer to do this
    writer.writerow([name, home]) #line we want to write to file
