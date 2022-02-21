#import necessary modules
from flask import Flask, render_template
import json
from bs4 import BeautifulSoup
import requests


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("selectors.json", 'r') as f:
        return json.load(f)

def my_scraper():
    # get the URL in a useable form
    url = "http://localhost:5000/scraping"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # select your objects
    elements = [elem for elem in soup.select('h1')]

    print(f"{len(elements)} Element(s) were found.")

    data = []

    for i, elem in enumerate(elements):
        data.append({"id": i, "name": elem.text.strip()})

    with open("data.json", 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()




# define route(s)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/webscraping")
def webscraping():
    return render_template("webscraping.html")

@app.route("/results")
def results():
    my_scraper()
    return render_template("results.html")

@app.route("/css-selectors")
def css-seletors():
    return render_template("css-selectors.html")

@app.route("/scraping")
def scraping():
    data = [
        {"strong": True, "content": "this text is bold"},
        {"strong": False, "content": "this is not bold"},
    ]
    return render_template("scraping.html", table=data)


# starts the webserver
if __name__ == "__main__":
    app.run()


