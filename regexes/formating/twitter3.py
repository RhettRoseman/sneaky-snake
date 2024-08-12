import re

url = input("URL: ")
# will tolerate http or https requests and www. or no www. requests | () tolerates anything inside the brackets 
# line 6 will ignore the twiiter link and only print whats left to find the username
username = re.sub(r"^(https?://)(www\.)twitter\.com$", "", url)
print(f"Username: {username}")
