from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

import data_lib

app = Flask(__name__)
app.url_map.strict_slashes = False
bootstrap = Bootstrap5(app)
data = data_lib.load()


@app.route("/")
def index():
    # Only display news for now.
    to_delete = set(data.keys()) - {"news"}
    for k in to_delete:
        del data[k]
    return render_template("index.html", data=data)
