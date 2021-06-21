# BeautifulSoup4

    BeautifulSoup는 HTML과 XML 문서를 파싱하기위한 파이썬 라이브러리/패키지이다.
    
    웹 스크래핑에 유용한 HTML에서 데이터를 추출하는 데 사용할 수있는 구문 분석 된 페이지에 대한 구문 분석 트리를 생성한다.

## BeautifulSoup3 vs BeautifulSoup4

    뷰티플수프 3용 코드는 하나만 살짝 바꾸면 뷰티플수프 4에도 작동한다. 꾸러미 이름을 BeautifulSoup에서 bs4로 바꾸기만 하면 된다.

    뷰티플수프 3는 파이썬의 SGMLParser해석기를 사용했다. 이 모듈은 파이썬 3.0에서 제거되었다.
    
    뷰티플수프 4는 기본으로 html.parser을 사용하지만, 대신에 lxml이나 html5lib을 설치해 사용할 수있다.

- ##  SGML(Standard Generalized Markup Language)

        표준 마크업 언어 규약(국제 표준으로 정한 마크업 언어)

        컴퓨터용 전자 문서의 작성에 관한 국제 표준 규약

        컴퓨터에서 쓰이는 전자문서를 작성함에 있어,
        이 전자문서가 어떠한 시스템 환경에서도 정보으 ㅣ손실없이 전송, 저장, 자동처리가 가능하도록 국제표준화기구(ISO)에서 정한 것이 SGML이다.

        HTML과 XML은 모두 SGML에 근거하여 만들어졌다.

- ##  HTML(Hyper-Text Markup Language)

        하이퍼 텍스트를 저장하기 위해서 개발된 언어

        웹 페이지 코드를 작성할 때 사용되는 언어

        HTML은 문서의 글자모양, 그림, 영상, 하이퍼링크 등을 지정하는 명령어이며 이러한 명령어를 태그라고 한다
- ##  XML(eXtensible Markup Language)
    
        확장형 마크업 언어로써 HTML의 업그레이드 버전   

        HTML이 문법 사용에 있어서 각각의 웹 브라우저에서 상호 호환되지않는 문제와 SGML의 복잡함을 해결하기 위해 개발되었다.

        XML은 주로 다른 시스템, 특히 인터넷에 연결된 시스템끼리 데이터를 쉽게 주고 받을 수 있게 하여 HTML의 한계를 극복할 목적으로 만들어졌다.

        HTML문서는 화면에 나타는 문서가 하나의 파일로 되어있지만, XML은 요소 별로 개별 파일로 구성되어 있기 때문에 문서를 요소 별로 저장, 검색, 재활용할 수 있다.

    [참고자료 - SGML/HTML/XML](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kimone0915&logNo=150119128236)

## Web Scraping

    웹 스크래핑은 웹 사이트에서 특정 데이터를 추출하는 데 사용되는 데이터 스크래핑입니다.
    
    웹 스크래핑 소프트웨어는 Hypertext Transfer Protocol 또는 웹 브라우저를 사용하여 World Wide Web에 직접 액세스 할 수 있습니다.

## Web Crawling

    일반적으로 “crawler”라는 용어는 명확한 최종 목표나 목표가 없어도 사이트나 네트워크가 제공할 수 있는 것을 끝없이 탐색하면서 스스로 웹 페이지를 탐색할 수 있는 프로그램의 능력을 의미한다.

    자동화 봇인 웹 크롤링가 정해진 규칙에 따라 복수 개의 웹 페이지를 브라우징하는 행위이다.

    웹 크롤러는 Google, Bing 등과 같은 검색 엔진에서 URL의 콘텐츠를 추출하고, 이 페이지에서 다른 링크를 확인하고, 링크의 URL을 가져오는 데 주로 사용된다.

# Example Python Code
```py
from bs4 import BeautifulSoup

url = "https://www.naver.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

soup.title
soup.title.get_text()
soup.a
soup.a.attr
soup.a["href"])
soup.find("a", attrs={"class":"Nbtn_upload"})
soup.find("h1")
soup.find_next_sibling("li")
soup.find_previous_sibling("li")
.
.
.
```