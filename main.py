from flask import Flask, render_template
import yt_dlp as yt
import re

app = Flask(__name__)
dl = yt.YoutubeDL()

@app.route("/")
def home():
    return render_template("index.html")

class DL:
    
    def download_video(self, link):
        pass

    def export_video(self, link):
        pass

    def import_video(self, link):
        pass
    
    @staticmethod
    def get_info(link):
        pass

    def check_syntax(self, link):
        return True if re.match(r"(www.youtube.com).*", link, re.IGNORECASE) else False

if __name__ == "__main__":
    app.run()