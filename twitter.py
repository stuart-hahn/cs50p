import re

url = input("URL: ").strip()

if matches := re.search(
    r"^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE
):
    username = matches.group(1)
    print(username)
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
