import re

url = input("Enter the URL: ").strip()

# Remove the url to extract username
# make a variable called matches in order to easily use the regex search function in the rest of code
matches = re.search(r"https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if else use the regex search function
if matches:
    # print the username
    print(f"Username: {matches.group(2)}")

#we can make this code better