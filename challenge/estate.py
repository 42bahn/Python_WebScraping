from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.naver.com/"

options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get(url)

search = driver.find_element_by_id("query")
search.send_keys("송파 헬리오시티")
search.send_keys(Keys.ENTER)

estate_banner = driver.find_element_by_class_name("sp_nland")

if estate_banner:
    estate_banner.find_element_by_class_name("name").click()
    driver.switch_to_window(driver.window_handles[1])
    item_list = driver.find_element_by_class_name("naver_logo")
    if item_list:
        items = driver.find_elements_by_class_name("item")
        count = 1
        for index, item in enumerate(items):
            item.click()
            time.sleep(1)
            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "detail_contents_inner")))
                soup = BeautifulSoup(driver.page_source, "lxml")
            finally:
                info = soup.find("div", attrs={"class":"detail_contents_inner"})
                title = info.find("strong", attrs={"class":"info_title_name"})
                type = info.find("span", attrs={"class":"type"})
                price = info.find("span", attrs={"class":"price"})
                
                table = info.find("table", attrs={"class":"info_table_wrap"}).find_all("tr")
                area = table[1].find("th", attrs={"scope":"row"}).get_text()
                area_value = table[1].find("td").get_text()
                floor = table[2].find("th", attrs={"scope":"row"}).get_text()
                floor_value = table[2].find("td").get_text()
                room = table[2].find("th", attrs={"scope":"row"}).find_next_sibling("th").get_text()
                room_value = table[2].find("td").find_next_sibling("td").get_text()
                monthly_fee = table[3].find("th", attrs={"scope":"row"}).get_text() + "(" + table[3].find("td").find_next_sibling("td").get_text() + ")"
                monthly_fee_value = table[3].find("td").get_text()
                feature = table[0].find("th", attrs={"scope":"row"}).get_text()
                feature_value = table[0].find("td").get_text()

                print("=======매물 {} =======".format(index + 1))
                if title:
                    print(f"이름 : {title.get_text()}")
                if type:
                    print(f"거래 : {type.get_text()}")
                if price:
                    print(f"가격 : {price.get_text()}")
                print(f"{area} : {area_value}")
                print(f"{floor} : {floor_value}")
                print(f"{room} : {room_value}")
                print(f"{monthly_fee} : {monthly_fee_value}")
                print(f"{feature} : {feature_value}")
                count += 1
                

