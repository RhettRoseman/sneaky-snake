# import re from python
import re

# ask user for email 
email = input("What's your name email? ").strip()

# if re.search contains @ print valid
# r in this case is a raw string just like f in the fstring means format 
# ^ means start of the string
# $ means end of the string
# + means one or more of the preceding character
# \ means treat the following literally
# . means one or more of the following characters

if re.search(r"^.*@.*\.edu$", email):
    print("Valid")
else:
    print("Invalid")
    
