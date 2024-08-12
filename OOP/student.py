# main function: ask the user for their name and house, then print the name and house
def main():
    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house} ")

# This function prompts the user to enter their name and returns the entered name
def get_name():
    name = input("Name: ")
    return name
# The function ends here, and the entered name can be used in the calling function or script.
def get_house():
    house = input("House: ")
    return house
# The function ends here, and the entered name can be used in the calling function or script.

# checks if the script is running correctly then calls the main function
if __name__ == "__main__":
    main()