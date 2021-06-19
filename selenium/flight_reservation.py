from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("selenium\chromedriver.exe")
browser.maximize_window()

url = "https://flight.naver.com/flights/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("26")[0].click()
browser.find_elements_by_link_text("27")[1].click()

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()

try:
    tickets = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "trip_result_list li")))
finally:
    for ticket in tickets:
        print("---------------------------------")
        print(ticket.text)
