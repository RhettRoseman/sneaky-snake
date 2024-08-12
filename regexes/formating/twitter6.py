import re 

url = input("URL: ").strip()
# ?: = dont capture this group we did with https:// the same as www. so the search will ignore both
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")
