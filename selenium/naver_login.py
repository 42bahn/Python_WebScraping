from selenium import webdriver

browser = webdriver.Chrome("selenium\chromedriver.exe")
browser.get("http://www.naver.com")

login = browser.find_element_by_class_name("link_login")
login.click()

id = browser.find_element_by_id("id")
id.send_keys("banijun")

pw = browser.find_element_by_id("pw")
pw.send_keys("ahngrv0704")