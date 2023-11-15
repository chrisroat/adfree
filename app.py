from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

import data_lib

app = Flask(__name__)
bootstrap = Bootstrap5(app)
data = data_lib.load()


@app.route("/")
def index():
    return render_template("index.html", data=data)
