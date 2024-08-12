url = input("URL: ")

# Extract the username from the URL string  by removing the prefix
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")