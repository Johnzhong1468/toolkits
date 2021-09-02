from flask import Flask, render_template, url_for, jsonify, session, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()