import re
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # WebDriver를 최대 10초까지 기다리는 객체
from selenium.webdriver.support import expected_conditions as EC

def init_webdriver(url):
    options = webdriver.ChromeOptions()
    options.headless = True # True == 웹 브라우저를 띄우지 않음 / False == 웹 브라우저를 띄움
    options.add_argument("window-size=1440,960") # 웹
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
    options.add_experimental_option('excludeSwitches', ['enable-logging']) # WebDriver 로드 시 터미널에 출력되는 로그 기록을 끔
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    driver.get(url)
    return (driver)

def init_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return (soup)

def remove_tag(tags):   # bs4를 통해 추출한 태그를 인자로 넘겨주어 해당 태그를 지워주는 함수
    for tag in tags:
        tag.decompose()

##################### Naver 날씨 정보 조회 ##########################
def naver_weather():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    
    ## Based on Selenium 
    # driver = init_webdriver()
    # driver.get(url)
    # try:
    #     WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "cs_weather")))
    # finally:
    #     soup = BeautifulSoup(driver.page_source, "lxml")
    ## end
    
    # Based on requests, bs4
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    # end

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
    print()
####################################################################


################# Naver 종합 헤드라인 뉴스 추출 ####################
def naver_total_news():
    url = "https://news.naver.com/"
    
    ## Based on Selenium 
    # driver = init_webdriver()
    # driver.get(url)

    # print(f"\n[{driver.find_element_by_class_name('tit_main1').text}]")
    # lists = driver.find_elements_by_class_name("hdline_article_list li")
    # for index, list in enumerate(lists): 
    #     if index == 3:
    #         break
    #     title = list.find_element_by_class_name("hdline_article_tit a")
    #     print(f"{title.text} (링크 : {title.get_attribute('href')})\n")
    ## end

    ## Based on requests, bs4
    soup = init_soup(url)
    
    print("[Naver 종합 헤드라인 뉴스]")
    lists = soup.find(class_="hdline_article_list").find_all("li") # class는 Python에서 예약어로 지정되어있기 때문에 class_(CSS 클래스) 키워드를 사용해야한다.
    for list in lists:
        head = list.find("div", attrs={"class":"hdline_article_tit"}).a
        title = head.get_text().strip()
        link = url + head['href']
        print(f"{title}\n(링크 : {link})\n")
    ## end
    print()
################### Naver IT 헤드라인 뉴스 추출#####################
def naver_IT_news():
    url = "https://news.naver.com"
    
    ## Based on Selenium 
    # driver = init_webdriver()
    # driver.get(url)
    # try:
    #     WebDriverWait(driver=driver, timeout=10).until(EC.presence_of_element_located((By.CLASS_NAME, "container")))
    # finally:
    #     print("\n[" + driver.find_element_by_xpath('//*[@id="snb"]/h2/a').text + " 헤드라인 뉴스]")
    #     driver.find_element_by_class_name("cluster_more").click()

    # head_line = driver.find_elements_by_class_name("cluster_head_topic a")
    # for line in head_line:
    #     print(line.text)
    #     print(f"링크 : {line.get_attribute('href')}\n")
    ## end

    print("[Naver IT 헤드라인 뉴스]")
    # Based on requests, bs4
    soup = init_soup(url + "/main/main.nhn?mode=LSD&mid=shm&sid1=105")
    lists = soup.find("div", attrs={"class":"_persist"}).find_all("h2", attrs={"class":"cluster_head_topic"})
    for list in lists:
        title = list.a.get_text().strip()
        link = url + list.a['href']
        print(f"{title}\n(링크 : {link})\n")
    # end
    print()
####################################################################

###############해커스 영어 사이트 오늘의 회화 데이터 추출##############
def hackers_convers():
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_gnb_eng_I_others_english&logger_kw=haceng_submain_gnb_eng_I_others_english"
    # # Based on Selenium
    # driver = init_webdriver(url)
        
    # print("[오늘의 회화]\n")
    # convs = driver.find_elements_by_class_name("conv_in")
    # for index, conv in enumerate(convs):
    #     if index == 0:
    #         print("한글 지문]")
    #     else:
    #         print("[영어 지문]")
    #     print(f"{conv.text}\n")
    # # end
    soup = init_soup(url)
    print("[오늘의 회화]\n")
    passages = soup.find_all("div", attrs={"class":"conv_txt"})
    for index, passage in enumerate(passages):
        if index == 0:
            print(">>>한글 지문")
        else:
            print(">>>영어 지문")
        sentences = passage.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
        for sentence in sentences:
            print(sentence.get_text().strip())
        print()
####################################################################

# Python main
if __name__ == "__main__":
    naver_weather()
    naver_total_news()
    naver_IT_news()
    hackers_convers()
