from flask import Flask,render_template
import json
app=Flask(__name__)
jogs=[
    {
        "id":1,
        "title":"data analyst",
        "location":"bengaluru,India",
        "salary":"Rs.10,000,000"
    },
    {
        "id":2,
        "title":"frontend engineer",
        "location":"bengaluru,India",
        "salary":"Rs.10,000,000"
    },
    {
        "id":3,
        "title":"data scientist",
        "location":"bengaluru,India",
        "salary":"Rs.10,000,000"
    },
    {
        "id":4,
        "title":"backend engineer",
        "location":"bengaluru,India",
        "salary":"Rs.10,000,0000"
    }
]
@app.route("/")
def hello():
    return render_template("home.html",jobs=jogs,company_name="salih")

@app.route("/api/jobs")
def list_jobs():
    return json(jogs)