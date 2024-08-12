url = input("URL: ")
# replace the url with nothing so we can just get the username
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

# this has some issues look for twitter2.py for a better solution