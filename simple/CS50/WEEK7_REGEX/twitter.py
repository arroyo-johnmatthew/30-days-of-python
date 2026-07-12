import re

url = input("URL: ").strip()
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Hello, {matches.group(1)}") 