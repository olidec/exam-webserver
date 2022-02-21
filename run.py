#import necessary modules
from flask import Flask, render_template
import json


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("selectors.json", 'r') as f:
        return json.load(f)


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scraping")
def home():
    return render_template("results.html")
def scraping():
    data = [
        {"strong": True, "content": "this text is bold"},
        {"strong": False, "content": "this is not bold"},
    ]
    return render_template("scraping.html", table=data)


# starts the webserver
if __name__ == "__main__":
    app.run()
# import necessary modules
from bs4 import BeautifulSoup
import requests
import json


def main():
    # get the URL in a useable form
    url = "http://local-host5000-scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')


    elements = [elem for elem in soup.select('h1')]

    print(f"{len(elements)} Element(s) were found.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()
