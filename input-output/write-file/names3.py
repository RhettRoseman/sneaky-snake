name = input("What is your name? ")


# 'with' statement automatically closes the file after its execution
# automates the process more pythonic 
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
