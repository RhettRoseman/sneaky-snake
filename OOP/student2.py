def main():
    name, house = get_student()
    print(f"Hello, {name} from {house}.")
    
def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    return name, house

if __name__ == "__main__":
    main()
    
# we have separated the code into two functions: main() and get_student().
# The main() function calls the get_student() function to get the name and house of the student.
# This makes the student.py a little bit more modular and easier to read.
# This way we make the code 11 lines instead of 19 lines.