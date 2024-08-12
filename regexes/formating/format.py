name = input("What's your name?").strip()

# Validate name
if ", " in name:
    # must have a comma but doesnt need a space 
    last, first = name.split(", ?")
    name = f"{first} {last}"
print(f"hello, {name}")

