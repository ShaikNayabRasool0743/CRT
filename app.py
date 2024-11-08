from flask import Flask # type: ignore

app=Flask(__name__)

app.route("/")
def homepage():
    return "day 1 code"