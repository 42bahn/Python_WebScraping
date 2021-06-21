# selenium

## [Selenium with Python](https://selenium-python.readthedocs.io/)

    셀레늄(Selenium)은 웹 애플리케이션 테스트를 위한 포터블 프레임워크이다.

    Selenium은 웹 브라우저의 자동화를 가능하게 하고 지원하는 다양한 도구와 라이브러리를 포함한 프로젝트이다.

    Selenium의 핵심은 WebDriver 이다. 
    이는 다양한 브라우저에서 호환 가능한 지시사항을 작성할 수 있는 인터페이스라 할 수 있다. 

- ## selenium 설치
    > pip install selenium
    
    브라우저별로 selenium webdriver를 다운로드해야 한다.

    [Google Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)  
    [Firefox](https://github.com/mozilla/geckodriver/releases)   
    [Microsoft Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
    [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

```py
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome('chromedriver')
driver.get(url='https://www.google.com/')
try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME , 'gLFyf'))
    )
finally:
    driver.quit()
```

[참고자료 - Python Selenium 사용법](https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/)