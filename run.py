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


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scraping")
def scraping():
    data = [
        {"strong": True, "content": "this text is bold"},
        {"strong": False, "content": "this is not bold"},
    ]
    return render_template("scraping.html", table=data)

@app.route ("/results")
def results():
    return render_template("results.html")

def my_scraper ():
    def main():
        # get the URL in a useable form
        url = "http://localhost:5000/scraping"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # select your objects
        elements = [elem for elem in soup.select('td')]

        print(f"{len(elements)} Element(s) were found.")

        data = []

        for i, elem in enumerate(elements):
            data.append({"id": i, "name": elem.text.strip()})

        with open("data.json", 'w') as f:
            json.dump(data, f, indent=4)


# starts the webserver
if __name__ == "__main__":
    app.run()
