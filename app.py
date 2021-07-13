from flask import Flask
from crawler import tjrj

app = Flask(__name__)


@app.route("/")
def hello_world():
    tjrj.get_info()
    return "<p>Hello, World!</p>"
