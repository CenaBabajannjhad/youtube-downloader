from flask import Flask, render_template
from helper import DL

app = Flask(__name__)
dl = DL()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/<link>")
def api_get(link):
    data = dl.get_info(link)
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()