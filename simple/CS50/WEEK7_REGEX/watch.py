import re

def main():
    print(parse(input("HTML: ")))

def parse(link):               #1     #2            #3     #4                #5
    matches = re.search(r'<iframe.+src="?(https?)(://)(?:www\.)?(youtu)(be)\.com/embed(/[a-zA-Z0-9]+)"?.+></iframe>', link)

    if matches:
        if matches.group(1).endswith("s"):
            return matches.group(1) + matches.group(2) + matches.group(3) + "." + matches.group(4) + matches.group(5)
        else:
           return matches.group(1) + "s" + matches.group(2) + matches.group(3) + "." + matches.group(4) + matches.group(5) 
    else:
        return None

if __name__ == "__main__":
    main()