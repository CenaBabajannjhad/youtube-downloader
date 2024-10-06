from flask import Flask, render_template
from helper import DL
import base64 

app = Flask(__name__)
dl = DL()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/<string:b64_url>", methods=['POST'])
def api_get(b64_url):
    
    encode_url = str(b64_url).replace("_", "/")
    decode_url = base64.b64decode(encode_url).decode("UTF-8")

    data = dl.get_info(decode_url)
    
    return data

if __name__ == "__main__":
    app.run()