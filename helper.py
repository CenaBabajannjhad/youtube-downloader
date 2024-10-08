import re
from yt_dlp import YoutubeDL


class DL:
    
    def __init__(self) -> None:
        ydl_opts = {'cookiesfrombrowser': ('firefox',), 'format' : 'mp4/bestvideo/best', 'outtmpl': "%(title)s.%(ext)s", 'proxy' : "127.0.0.1:1089"}
        self._ydl = YoutubeDL(ydl_opts)

    # decorator for check url is valid or not
    def _check(func):
        
        def wrapper(self, link):            
            is_valid = any(re.match(regex, link, re.IGNORECASE) for regex in [r".*(www\.youtube\.com).*", r".*(youtu\.be).*"])
    
            if is_valid:
                return func(self, link)
            return None    
        
        return wrapper

    @_check
    def get_info(self, link):

        data = {}
        info_dict = self._ydl.extract_info(f"{link}", download=False)
        video_url = info_dict.get("url", None)
        video_title = info_dict.get("title", "")
        data.__setitem__(f"{0}", {"url" : video_url, "title" : video_title})

        return data
    
    def export_video(self, link):
        pass

    def import_video(self, link):
        pass

    @_check
    def is_playlist(self, link):
        if "playlist" in link:
            return True
        return False