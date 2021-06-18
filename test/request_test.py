import requests

url = "http://nadocoding.tistory.com"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}

res = requests.get(url, header)
res.raise_for_status()

print("WEB Scraping...")

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)