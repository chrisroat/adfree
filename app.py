from flask import Flask, abort, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)


@app.route("/")
def index():
    fmt = request.args.get("format", "carousel")
    if fmt not in ["carousel", "list"]:
        return abort(404)
    return render_template(f"{ fmt }.html", data=DATA)


DATA = {
    "podcast": [
        {
            "title": "Freakonomics",
            "homepage": "https://freakonomics.com",
            "signup": "https://freakonomics.com/plus/",
            "img": "https://freakonomics.com/wp-content/themes/freakonomics_2021/images/plus_logo_2.png",
        },
        {
            "title": "Mindscape",
            "homepage": "https://www.preposterousuniverse.com/podcast/",
            "signup": "https://www.patreon.com/seanmcarroll",
            "img": "https://www.preposterousuniverse.com/wp-content/uploads/SCM-rectangle-medium-1.jpg",
        },
    ],
    "news": [
        {
            "title": "The Guardian",
            "homepage": "https://www.theguardian.com/us",
            "signup": "https://support.theguardian.com/us/contribute",
            "img": "https://pbs.twimg.com/profile_banners/788524/1542015319/1500x500",
        },
        {
            "title": "San Jose Mercury News",
            "homepage": "https://www.mercurynews.com/",
            "signup": "https://checkout.mercurynews.com/subscriptionmultiproductpw",
            "img": "https://s3.amazonaws.com/cms.mngcep/TMN_logo_620x76-01.png",
        },
    ],
}
