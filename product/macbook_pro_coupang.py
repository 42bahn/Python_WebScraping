import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/promotion/94162"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

macbooks = soup.find_all("li", attrs={"class":"baby-product"})

for macbook in macbooks:
    name = macbook.find("div", attrs={"class":"name"}).get_text()

    price_info = "가격 : " + macbook.find("strong", attrs={"class":"price-value"}).get_text()
    price = 0
    if macbook.find("span", attrs={"class":"price-info"}):
        base_price = macbook.find("del", attrs={"class":"base-price"})
        dc_percent = macbook.find("span", attrs={"class":"discount-percentage"})
        if base_price:
            price_info += "(정가 : " + base_price.get_text()
            if dc_percent:
                price_info += ", " + dc_percent.get_text() + ")"
            else:
                price_info += ")"
    
print(name, price_info)