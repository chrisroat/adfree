from flask import Flask, abort, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route("/")
def index():
    return render_template(f"index.html", data=DATA)


DATA = {
    "podcast": [
        {
            "title": "Astronomy Cast",
            "homepage": "https://www.astronomycast.com/",
            "signup": "https://www.patreon.com/astronomycast",
        },
        {
            "title": "Freakonomics",
            "homepage": "https://freakonomics.com",
            "signup": "https://freakonomics.com/plus/",
        },
        {
            "title": "Mindscape",
            "homepage": "https://www.preposterousuniverse.com/podcast/",
            "signup": "https://www.patreon.com/seanmcarroll",
        },
    ],
    "news": [
        {
            "title": "The Guardian",
            "homepage": "https://www.theguardian.com/us",
            "signup": "https://support.theguardian.com/us/contribute",
        },
        {
            "title": "San Jose Mercury News",
            "homepage": "https://www.mercurynews.com/",
            "signup": "https://checkout.mercurynews.com/subscriptionmultiproductpw",
        },
    ],
}
