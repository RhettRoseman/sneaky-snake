import re 

email = input("What's your email? ").strip()
# if re.search contains @ print valid
# r in this case is a raw string just like f in the fstring means format 
# ^ means start of the string
# $ means end of the string
# + means one or more of the preceding character
# \ means treat the following literally
# . means one or more of the following characters
# [^@]+ means any character except an @ sign
if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")