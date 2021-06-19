from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

browser = webdriver.Chrome("selenium\chromedriver.exe")
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("26")[0].click()
browser.find_elements_by_link_text("27")[1].click()

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()

filename = "티켓.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

try:
    tickets = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "trip_result_list li")))
finally:
    for ticket in tickets:
        print("---------------------------------")
        print(ticket.text)
