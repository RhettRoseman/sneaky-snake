import re 

email = input("What's your email? ").strip()
# if regularexpression.search contains a word/number/underscore @ word/number/underscore with  .com print valid
# re.IGNORECASE = ignore the case of the expression 


if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")