from flask import Flask, render_template, request, redirect, url_for, session
import requests
import config
import random

# Flask
app = Flask(__name__)

# Flask route
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    params = request.get_json()
    query = params["query"]
    # url = f"https://unsplash.com/napi/search/photos?query={query}&xp=&per_page=2&page={page}"
    url = f"https://api.unsplash.com/search/photos?query={query}&client_id={config.US_ACCESSKEY}"
    response = requests.get(url)
    if response.status_code == 200:
        photos = response.json()
        photo = pick_photo(photos)
        return photo
    else:
        return None


def pick_photo(photos):
    return random.choice(photos["results"])



app.run(host="0.0.0.0", port=5000, debug=True)