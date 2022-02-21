#import necessary modules
from flask import Flask, render_template
import json


# set up flask webserver
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def load_selectors():
    with open("data.json", 'r') as f:
        return json.load(f)


# define route(s)
@app.route("/")
def home():
    return render_template("index.html")


# define route(s)
@app.route("/results")
def results():
    data = [
    {
        "id": 0,
        "name": "this text is bold"
    },
    {
        "id": 1,
        "name": "this is not bold"
    }
    ]
    return render_template("results.html", data=load_selectors())

@app.route("/scraping")
def scraping():
    data = [
        {"strong": True, "content": "this text is bold"},
        {"strong": False, "content": "this is not bold"},
    ]
    return render_template("scraping.html", data=data)

@app.route("/css-selectors")
def css_selectors():
    return render_template("css-selectors.html", selectors=load_selectors())



# starts the webserver
if __name__ == "__main__":
    app.run()
