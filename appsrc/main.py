from flask import Flask, render_template, url_for, jsonify, session
import pandas as pd
import numpy as np

app = Flask(__name__)
TABLIST = ["tab1", "tab2"]


@app.route('/', methods=["GET", "POST"])
def homepage():
    return render_template("index.html", tablist=TABLIST)

@app.route('/tab1')
def tab1():
    return render_template("tab1.html", tablist=TABLIST)

@app.route('/tab2')
def tab2():
    return render_template("tab2.html", tablist=TABLIST)


if __name__ == "__main__":
    app.run()
