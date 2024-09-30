from flask import Flask, render_template
import yt_dlp as yt
import re

app = Flask(__name__)
dl = yt.YoutubeDL()

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()