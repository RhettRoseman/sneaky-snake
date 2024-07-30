email = input("What's your email?").strip()

# Check if email contains an "@" and a "."
# if @ and . are in the user input then it is valid
if "@" and "." in email:
    print("Valid")
else:
    print("Invalid")

# still not perfect check validate2.py