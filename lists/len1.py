# Declare variables
student = ["John", "Jennie", "Jim", "Jack", "Joe"]

# range takes a number and len is the lengeth value# range takes a number and len is the lengeth value
for i in range(len(student)):
    # print number of array and the name of the student and add 1 to start from 1 when rendered 
    print(i + 1, student[i])

    # expect output:
                    # 1 John
                    # 2 Jennie
                    # 3 Jim
                    # 4 Jack
                    # 5 Joe