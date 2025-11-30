import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

for i, a in enumerate(soup.select(".titleline a")[:10], 1):
    print(f"{i}. {a.text}")
