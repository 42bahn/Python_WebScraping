# requests Module

## Requests Module

    간편한 HTTP 요청처리를 위해 사용하는 모듈

    웹페이지에서 HTTP 요청을 보내 원하는 HTML 정보를 가져오는 모듈이다.

    기본 내장 모듈이 아니기 때문에 개발자가 별도로 설치해주어야 한다. 
 
## GET & POST
```py
import requests

r = requests.get('https://www.google.com')
r = requests.post('https://httpbin.org/post', data = {'key':'value'})
```

## Passing Parameters In URLs
```py
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
```

## requests.raise_for_status()

200(OK / SUCCESS) 코드가 아닌 경우 에러 발동

```py
import requests

url = "..."
res = requests.get(url)
res.raise_for_status()
```

[참고자료 - requests User Guide](https://2.python-requests.org/en/master/user/quickstart/#make-a-request)