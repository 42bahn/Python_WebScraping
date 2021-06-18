import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 요일 웹툰 전체 가져오기
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())