from flask import Flask, render_template
import youtube_dl as yt

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()