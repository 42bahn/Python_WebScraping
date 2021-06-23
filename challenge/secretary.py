from selenium import webdriver

from selenium.webdriver.common.keys import Keys # 키보드 입력에 대한 이벤트 처리

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait # WebDriver를 최대 10초까지 기다리는 객체
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

# bs4를 통해 추출한 태그를 인자로 넘겨주어 해당 태그를 지워주는 함수
def remove_tag(tags):
    for tag in tags:
        tag.decompose()

options = webdriver.ChromeOptions()
options.headless = True # 웹 브라우저를 띄우지 않음
options.add_argument("window-size=1440,960")
options.add_experimental_option('excludeSwitches', ['enable-logging']) # WebDriver 로드 시 터미널에 출력되는 로그 기록을 끔
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

url = "https://www.naver.com/"

##################### Naver 날씨 정보 조회 ##########################
driver.get(url)
search = driver.find_element_by_id("query")
search.send_keys("날씨")
search.send_keys(Keys.ENTER)

try:
    section = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "cs_weather")))
finally:
    soup = BeautifulSoup(driver.page_source, "lxml")
    remove_tag(soup.find_all("span", attrs={"class":"blind"}))
    
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
####################################################################


######################헤드라인 종합/IT 뉴스 추출######################
driver.get(url)
driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[2]/a').click()

head_line = driver.find_element_by_id("today_main_news")
print(f"\n[{driver.find_element_by_class_name('tit_main1').text}]")

lists = driver.find_elements_by_class_name("hdline_article_list li")
for index, list in enumerate(lists): 
    if index == 3:
        break
    title = list.find_element_by_class_name("hdline_article_tit a")
    print(f"{title.text} (링크 : {title.get_attribute('href')})\n")

# IT 뉴스 추출
driver.find_element_by_xpath('//*[@id="lnb"]/ul/li[8]/a').click()
try:
    WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
finally:
    soup = BeautifulSoup(driver.page_source, "lxml")
    print("\n[" + driver.find_element_by_xpath('//*[@id="snb"]/h2/a').text + " 헤드라인 뉴스]")
    driver.find_element_by_class_name("cluster_more").click()

head_line = driver.find_elements_by_class_name("cluster_head_topic a")
for line in head_line:
    print(line.text)
    print(f"링크 : {line.get_attribute('href')}\n")
####################################################################

###############해커스 영어 사이트 오늘의 회화 데이터 추출##############
driver.get("https://www.hackers.co.kr/")
try:
    ad = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.ID, "main_breand")))
finally:
    ad.find_element_by_id("main_breand_checkbox_close2").click()

try:
    header = WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.ID, "header")))
finally:
    link = header.find_element_by_class_name("mn01 a").get_attribute('href')
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/div[1]/div[2]/pre/dl[1]/dd/ul/li[8]/a').click()
    
print("[오늘의 회화]")
convs = driver.find_elements_by_class_name("conv_in")
for index, conv in enumerate(convs):
    if index == 0:
        print("[한글 지문]")
    else:
        print("[영어 지문]")
    print(f"{conv.text}\n")
####################################################################