email = input("What is your email address?: ").strip()

# Validate the email address using regular expressions
username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("invalid")
    
