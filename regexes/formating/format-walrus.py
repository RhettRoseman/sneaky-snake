import re  # Import the regular expressions module

# Get the user's name as input
name = input("What's your name? ")

# Use a regular expression to match the pattern "last name, first name"
if matches := re.search(r"^(.+), ?(.+)$", name):
    # If the pattern matches, reformat the name to "first name last name"
    name = matches.group(2) + " " + matches.group(1)
    # Print the formatted name
    print(f"Hello, {name}")
else:
    # If the pattern doesn't match, print an error message
    print("Invalid name")