from bs4 import BeautifulSoup
from requests import get
from re import match
from urllib.parse import quote
from sys import stdout


def save_content(content, title):
    with open(f"C:\\Users\\Ben Donnelly\\Desktop\\4th Year\\Semester2\\paralell\\Assignment_4\\{title}.html", "w") as f:
        f.write(content)
        f.close()


def main():
    start_site = get("https://www.imdb.com/")

    parser = BeautifulSoup(start_site.text, "html.parser")

    # Append start site to link list
    links = [start_site.url]

    # find all 'a' tags
    for anchor_tags in parser.find_all('a'):
        # actually a link
        if anchor_tags.has_attr('href'):
            link = anchor_tags['href']
            # could be a standalone link or a continuation
            # If continuation pre-append original link
            links.append(link) if match('^http(s)*', link) else links.append(f"{start_site.url}{link}")
    # Getting payload of those links
    # Progress counter
    for count, link in enumerate(links):
        progress = f"Obtaining site {link}\nProgress: {int((count+1)/len(links) * 100)}%"
        stdout.write("\b" * len(progress) + progress)
        stdout.flush()

        next_site = get(link)
        parser = BeautifulSoup(next_site.text, "html.parser")
        # Calls file writing function
        # sanitises links so they can be the names of the files
        # if link length is too long you get an error
        # truncate to 50 characters (if over 50) for safety and avoid error
        save_content(str(parser.encode('utf-8')), quote(link[:50], ''))


if __name__ == '__main__':
    main()
