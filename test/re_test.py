import re

p = re.compile("ca.e")  # 정규 표현식 패턴을 정규식 객체로 컴파일

def print_match(m):
    if m:
        print("m.group() : ", m.group()) # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 인덱스
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 인덱스
        print("m.span() : ", m.span()) # 일치하는 문자열의 인덱스 좌표 (시작, 끝)
    else:
        print("Not matched")

# m = p.match("good care")
# m = p.search("good care") 
lst = p.findall("good care") 

# match() : 100% 일치하는 문자열을 찾는 함수
# search() : 일부 일치하는 문자열을 찾는 함수
# findall() : 일치하는 모든 문자열을 리스트 형으로 반환

# print_match(m)
print(lst)
