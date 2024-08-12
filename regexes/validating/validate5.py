import re 

email = input("What's your email? ").strip()
# if re.search contains @ print valid
# this version allows certain characters in the email address before/after the @ and the .edu domain
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")