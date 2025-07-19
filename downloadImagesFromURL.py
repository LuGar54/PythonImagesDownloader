from bs4 import BeautifulSoup
from urllib.request import urlopen
from os.path  import basename
import requests

base_url = "https://www.combatcamera.forces.gc.ca/site/"
page_url = "index-eng.asp"
page = urlopen(base_url + page_url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
images = soup.find_all("img")

print(images)
for image in images:
    lnk = base_url + image["src"]
    with open('images/' + basename(lnk), "wb") as f:
        f.write(requests.get(lnk).content)