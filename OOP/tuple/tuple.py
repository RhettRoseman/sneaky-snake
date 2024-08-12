# main function prints out the name and house of the student.
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # return tuple 
    return (name, house) # <= this is a tuple

if __name__ == "__main__":
    main()