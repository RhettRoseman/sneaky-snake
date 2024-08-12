import re 

email = input("What's your email? ").strip()
# if re.search contains a word/number/underscore @ word/number/underscore with either .com or .edu print valid


if re.search(r"^\w+@\w+\.(com|edu)$", email):
    print("Valid")
else:
    print("Invalid")