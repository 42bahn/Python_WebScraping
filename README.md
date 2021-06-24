# Python

## [1.  re](./re)

## [2.  requests](./requests)

## [3.  BeautifulSoup4](./BeautifulSoup4)
* ### [Webtoon](./webtoon) / [Product](./product)

## [4.  CSV](./csv)
* ### [Stock](./csv/csv_stock.py)

## [5.  Selenium](./selenium)
* ### [Naver Login](./selenium/naver_login.py) / [Youtube](./selenium/brave_girls_youtube.py) / [Flight Reservation](./selenium/flight_reservation.py) / [Google Movie](./selenium/google_movie.py)

## [6.  Challenge](./challenge)
* ### [estate](./challenge/estate.py) / [secretary](./challenge/secretary.py)

## 개발 참고 문서
* # [Selenium with Python](https://selenium-python.readthedocs.io/)
* # [https://www.selenium.dev/documentation/ko/](https://www.selenium.dev/documentation/ko/)

## Module & Package

    모듈이란 각종 변수, 함수, 클래스를 담고있는 파일
    특정 기능을 .py 확장자로, 파이썬 프로그래밍 언어 형식으로 작성된 파일로 작성

    이러한 모듈을 여러 개 모아놓은 것을 패키지라 한다.

    ex)
    import 모듈이름 [as 별칭]
    import re
    import requests as req
    
    from 키워드를 통해 모듈안의 일부인 변수, 함수, 클래스를 가져올 수 있다.

    ex)
    from selenium import webdriver

## BeautifulSoup vs Selenium
[참고블로그](https://ssamko.tistory.com/27)

    Python으로 크롤링(웹 스크래핑)을 할 때 BeautifulSoup는 굉장히 강력한 도구이다.

    하지만 동적페이지 중 데이터를 따로 받아서 완성시키는 페이지들은 BeautifulSoup으로 가져오려고 하면 
    엉뚱한 데이터들이 가져와지거나 실패하는 경우가 종종 생긴다. 

    물론 그런 페이지들도 BeautifulSoup을 집요하게 파고들면 스크랩이 가능한 것 같지만,  
    selenium을 이용하면 훨씬 간단하게 그런 페이지들을 스크래핑 할 수 있다.

    selenium은 chrome을 이용해 실제 페이지를 띄우고 우리가 키보드 마우스로 하는 동작들을 자동화해주는 라이브러리이다.
 
| BeautifulSoup | Selenium |
| --- | --- |
| html 정보 파싱 | 웹 동작 |
| HTML, XML 파일의 정보를 추출해내는 python 라이브러리 | 자동화 테스트에 사용되는 프레임워크 |
| Python 내장 모듈 requests나 urllib을 이용해 HTML을 다운 받고, BeautifulSoup으로 테이터를 추출한다.  | 셀레늄을 이용한 크롤러는 웹 페이지에서 javascript 렌더링을 통해 생성되는 데이터들을 손쉽게 가져올 수 있다. |
| 서버에서 HTML을 다운 받기 때문에 서버사이드 렌더링을 사용하지 않는 SPA 사이트나, <br> javascipt 렌더링을 필요로 하는 사이트들은 크롤링하기 까다롭다. | 동적 크롤링을 효과적으로 수행하지만 라이브러리가 무거움 |
| Selenium과 비교적 빠르게 요청하고 스크래핑할 수 있다. | 웹 브라우저를 실제로 진행시키는 방법이기 때문에 속도도 많이 느리고, 메모리도 상대적으로 많이 차지한다. |
| requests, BeautifulSoup | webdriver(By, WebDriverWait, expected_conditions ...) |

- 참고 블로그
    * [selenuim 과 requests 비교](https://mycup.tistory.com/270)  
    * [Selenium VS BeautifulSoup 라이브러리 비교](https://rladuddms.tistory.com/64)  
    * [Beautifulsoup vs Selenium](https://velog.io/@zoeyul/webcrawling)