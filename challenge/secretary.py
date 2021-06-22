from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

url = "https://www.naver.com/"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1440,960")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get(url)

#################### Naver 날씨 정보 조회 ####################
search = driver.find_element_by_id("query")
search.send_keys("날씨")
search.send_keys(Keys.ENTER)

try:
    section = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "cs_weather")))
finally:
    soup = BeautifulSoup(driver.page_source, "lxml")
    
    blinds = soup.find_all("span", attrs={"class":"blind"})
    for blind in blinds:
        blind.decompose()
    
    today = soup.find("div", attrs={"class":"main_info"})
    current = today.find("span", attrs={"class":"todaytemp"}).get_text() + today.find("span", attrs={"class":"tempmark"}).get_text()
    cast = today.find("p", attrs={"class":"cast_txt"}).get_text()
    print("[오늘의 날씨]")
    print(f"현재 온도 : {current}")
    print(f"{cast}")

    weekly = soup.find("div", attrs={"class":"_weeklyWeather"})
    am_rain_rate = weekly.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    pm_rain_rate = weekly.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()
    print(f"오전 강수 확률 : {am_rain_rate} / 오후 강수 확률 : {pm_rain_rate}\n")

    dust_info = soup.find("div", attrs={"class":"sub_info"})
    for dust in dust_info.find_all("dt"):
        value = dust.find_next_sibling("dd").get_text()
        print(f"{dust.get_text()} : {value}")



#############################################################


######################헤드라인 뉴스 추출######################

driver.get(url)
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]').click()

head_line = driver.find_element_by_id("today_main_news")
print(f"\n[{driver.find_element_by_class_name('tit_main1').text}]")

lists = driver.find_elements_by_class_name("hdline_article_list li")
for index, list in enumerate(lists):
    if index == 3:
        break
    title = list.find_element_by_class_name("hdline_article_tit a")
    print(f"{title.text} (링크 : {title.get_attribute('href')})")