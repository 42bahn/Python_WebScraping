import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attr)
# print(soup.a["href"])
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find(attrs={"class":"Nbtn_upload"}))

rank1 = soup.find("li", attrs={"class":"rank01"})
print("1위", rank1.a.get_text())

# rank2 = rank1.next_sibling.next_sibling
rank2 = rank1.find_next_sibling("li")
print("2위", rank2.a.get_text())

# rank3 = rank2.next_sibling.next_sibling
rank3 = rank2.find_next_sibling("li")
print("3위", rank3.a.get_text())

# print(rank3.previous_sibling.previous_sibling.a.get_text())
# print(rank3.fine_previous_sibling("li"))

# print(rank3.parent)

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="독립일기-100화 독립을 돌아보며")
print(webtoon)