import os, subprocess, zipfile, sys, shutil, time

launch_path = os.path.dirname(os.path.abspath(__file__))

try: os.mkdir(os.path.join(launch_path, "data"))
except Exception: pass
try: os.mkdir(os.path.join(launch_path, "driver"))
except Exception: pass

proc = subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium", "requests"])

import requests

def dl_it(p, s):
    if(len(s) > 0):
        req = requests.get(s, stream = True)
        if req.status_code < 300:
            with open(p, "wb") as f: 
                for chunk in req.iter_content(chunk_size=64000):
                    f.write(chunk)
        else: print("Couldn't download '{0}'".format(s))

def dl_list(d, l):
    for i in l:
        p = os.path.join(launch_path, d, i.split("/")[-1])
        if d == "": p = os.path.join(launch_path, i.split("/")[-1])

        dl_it(p, i)
        if p.endswith(".zip"):
            with zipfile.ZipFile(p, 'r') as zip_ref:
                   zip_ref.extractall(os.path.dirname(p))
            os.unlink(p)
        if p.endswith(".tar.gz"):
            with tarfile.open(p, "r:gz") as tar:
                tar.extractall()
            with tarfile.open(p[:-3], "r:") as tar:
                tar.extractall()
            os.unlink(p)
            os.unlink(p[:-3])

script = "https://raw.githubusercontent.com/Kreavita/i-watch-these-vods/master/vodwatcher.py"
dl_list("", [script])


sources_vods = "https://raw.githubusercontent.com/Kreavita/i-watch-these-vods/master/data/sources_vods"
index = "https://raw.githubusercontent.com/Kreavita/i-watch-these-vods/master/data/index"

dl_list("data", [sources_vods])


if os.name == "nt":
    url_gecko = "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip"
    url_chrome = "https://chromedriver.storage.googleapis.com/83.0.4103.14/chromedriver_win32.zip"
else:
    url_gecko = "https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz"
    url_chrome = "https://chromedriver.storage.googleapis.com/83.0.4103.14/chromedriver_linux64.zip"

dl_list("driver", [url_gecko, url_chrome])
