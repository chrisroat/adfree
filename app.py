from flask import Flask, abort, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route("/")
def index():
    return render_template("index.html", data=DATA)


DATA = [
    {
        "kind": "podcast",
        "subject": ["astronomy"],
        "title": "Astronomy Cast",
        "homepage": "https://www.astronomycast.com/",
        "signup": "https://www.patreon.com/astronomycast",
    },
    {
        "kind": "podcast",
        "subject": ["astronomy"],
        "title": "Universe Today",
        "homepage": "https://www.universetoday.com/",
        "signup": "https://www.patreon.com/universetoday",
    },
    {
        "kind": "podcast",
        "subject": ["economics"],
        "title": "Freakonomics",
        "homepage": "https://freakonomics.com",
        "signup": "https://freakonomics.com/plus/",
    },
    {
        "kind": "podcast",
        "subject": ["cosmology", "physics", "philosophy"],
        "title": "Mindscape",
        "homepage": "https://www.preposterousuniverse.com/podcast/",
        "signup": "https://www.patreon.com/seanmcarroll",
    },
    {
        "kind": "news",
        "subject": ["global news"],
        "title": "The Guardian",
        "homepage": "https://www.theguardian.com/us",
        "signup": "https://support.theguardian.com/us/contribute",
    },
    {
        "kind": "news",
        "subject": ["regional news"],
        "title": "San Jose Mercury News",
        "homepage": "https://www.mercurynews.com/",
        "signup": "https://checkout.mercurynews.com/subscriptionmultiproductpw",
    },
]
