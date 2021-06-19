from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("selenium\chromedriver.exe")
browser.get("https://www.youtube.com/")

# browser.back()
# browser.forward()
# browser.refresh()

# login = browser.find_element_by_class_name("link_login")
# login.click()

search = browser.find_element_by_id("search")
search.send_keys("브레이브 걸스")
search_key = browser.find_element_by_xpath("//*[@id='search-icon-legacy']")
search_key.click()

lists = browser.find_elements_by_tag_name("ytd-video-renderer a")
lists[0].click()
# for list in lists:
#     print(list)


