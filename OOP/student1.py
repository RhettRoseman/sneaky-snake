# defining the main function
def main():
    # Prompt the user to enter their name
    name = input("Enter your name: ")
     # Prompt the user to enter their house
    house = input("Enter your house: ")
    # Print the name and house
    print(f"Hello, {name} from {house}.")
    
def get_student():
    # Prompt the user to enter their name
    name = input("Enter your name: ")
    # Prompt the user to enter their house
    house = input("Enter your house: ")
    # Return the name and house
    return name, house

if __name__ == "__main__":
    main()
    