from flask import Flask, render_template, url_for, jsonify, session, request
import pandas as pd
import numpy as np

import updateIntervalDisplayAppUtils

app = Flask(__name__)

### Parameters ###
TABLIST = ["tab1", "tab2", "interval_update"]
# refresh freq (sec)
FREQ = 3

### APP Secret ###
app.secret_key = "custom_secret_key"

@app.route('/', methods=["GET", "POST"])
def homepage():
    return render_template("index.html", tablist=TABLIST)

@app.route('/tab1')
def tab1():
    return render_template("tab1.html", tablist=TABLIST)

@app.route('/tab2')
def tab2():
    return render_template("tab2.html", tablist=TABLIST)

# interval update display app
@app.route('/_updateData', methods=["POST"])
def updateData():
    if "SELECTED_TABLE" in session:
        data = updateIntervalDisplayAppUtils.get_data(session["SELECTED_TABLE"])
    else:
        data = updateIntervalDisplayAppUtils.get_data()
    return data.to_html(index=False)

@app.route('/interval_update', methods=["GET", "POST"])
def interval_update():
    selected_table_form = updateIntervalDisplayAppUtils.table_select_form(request.form)
    session["SELECTED_TABLE"] = selected_table_form.selected_table.data
    return render_template("interval_update.html", freq=FREQ, form=selected_table_form, tablist=TABLIST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
