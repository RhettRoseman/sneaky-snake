# validate users email address
# prompt for email address strip whitespace
email = input("What's your email?").strip()

# check if email is in correct format
if "@" in email:
    print("Valid")
else:
    print("Invalid")
    
# this will work for detecting @ symbols in email addresses but it's not a perfect solution
# check validate1.py