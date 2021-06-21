# CSV 

    몇 가지 필드를 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일이다. 
    
    확장자는 .csv이며 MIME 형식은 text/csv이다. comma-separated variables라고도 한다.

## csv Module

    csv 모듈은 CSV 형식의 표 형식 데이터를 읽고 쓰는 클래스를 구현한다.

    프로그래머는 다른 응용 프로그램에서 이해할 수 있는 CSV 형식을 기술하거나 자신만의 특수 용도 CSV 형식을 정의할 수 있다.

    csv 모듈의 reader와 writer 객체는 시퀀스를 읽고 쓴다. 
    
    프로그래머는 DictReader와 DictWriter 클래스를 사용하여 딕셔너리 형식으로 데이터를 읽고 쓸 수 있다.

- ## csv.reader(file)

    ```py
    import csv
 
    f = open('data.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        print(line)
    f.close()  
    ```

- ## csv.writter(file)

    ```py
    import csv   

    f = open('output.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([1, "세종대왕", False])
    wr.writerow([2, "이순신", True])
    f.close()
    ```

    [참고자료 - csv 파일 사용하기](http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)