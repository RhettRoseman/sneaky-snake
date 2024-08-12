import re  # Import the regular expressions module

# Get the user's name as input and strip any leading/trailing whitespace
name = input("What's your name? ").strip()

# Use a regular expression to match the pattern "last name, first name"
matches = re.search(r"^(.+), ?(.+)$", name)

# If there's a match, it means the input is in the "last name, first name" format
if matches:
    # Group 1 is the last name (.+) and group 2 is the first name (.+)
    last = matches.group(1)  # Extract the last name
    first = matches.group(2)  # Extract the first name
    # Reformat the name to "first name last name"
    name = f"{first} {last}"

# Print the formatted name using an f-string
print(f"Hello, {name}")