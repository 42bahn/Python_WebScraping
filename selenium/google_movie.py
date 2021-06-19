import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://play.google.com/store/movies/top"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
browser = webdriver.Chrome(executable_path="selenium\chromedriver.exe", options=options)
browser.maximize_window()
browser.get(url)

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == current_height:
        print("스크롤 완료")
        browser.get_screenshot_as_file("selenium/google_movie.png")
        break
    prev_height = current_height

soup = BeautifulSoup(browser.page_source, "lxml")

# 구글 영화 인기 차트 전체 목록 조회 - 영화 제목 추출 
# 
# movies = soup.find_all("div", attrs={"class":"uMConb"})
# print("영화 인기 차트 - " + str(len(movies)))
# print("====================================================================")
# for movie in movies:
#     title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).attrs['title']
#     print(title)


# 구글 영화 인기 차트 중 할인 영화 목록 조회 - 할인 영화 정보 추출 (제목, 정가 및 세일가, 링크)
movies = soup.find_all("div", attrs={"class":"uMConb"})
print("할인 영화 인기 차트")
print("=" * 100)

for movie in movies:
    if movie.find("span", attrs={"class":"SUZt4c djCuy"}):
        title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).attrs['title']
        cost = movie.find("span", attrs={"class":"SUZt4c djCuy"}).get_text()
        sale = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
        link = "https://play.google.com" + movie.find("a", attrs={"class":"JC71ub"})['href']     
        print(f"영화 제목 : {title}")
        print(f"구입가 : {cost} -> {sale}")
        print(f"링크 : {link}")
        print("-" * 100)

browser.quit()