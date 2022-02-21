# import necessary modules
from bs4 import BeautifulSoup
import requests
import json


def main():
    # get the URL in a useable form
    url = "http://localhost:5000/scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # select your objects
    elements = [elem for elem in soup.select('h1')]
    table rows = [elem for elem in soup.select{'scrape-this'}] <strong>
    
     tag = doc.find ("<strong>")
     print(tags.find_all("b"))

    print(f"{len(elements)} Element(s) were found.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})
        selectors.append

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
