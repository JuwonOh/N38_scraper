# N38_scraper

스팀슨 센터(Stimson Center)산하의 연구기관인 38North의 article(https://www.38north.org/articles/)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py, parser.py, downloader.py 그리고 scraping_latest_news.py 총 다섯가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리하는 등 scraper가 필요한 기본적인 기능을 가지고 있습니다.
parser.py는 모아진 url리스트를 통해서 각 분석들의 제목/일자/내용 등의 문자, 시간 데이터들을 parsing 합니다.
scraper.py는 사이트내의 url 링크들을 get_soup함수를 통해 모아주고, parser를 통해서 json형식으로 변환시킵니다.
downloader.py는 reserch paper와 Brookings papers on economy activity article의 pdf파일을 다운로드 하는 파일입니다.
scraping_latest_news.py는 scraper.py를 통해 만들어진 json파일을 저장시켜줍니다. scraping_latest_news.py파일의 parameter는 다음과 같습니다.

Using Python script with arguments

| Argument name | Default Value | Note |
| --- | --- | --- |
| begin_date | 2018-07-01 | datetime YYYY-mm-dd |
| directory | ./output/ | Output directory |
| max_num | 1000 | Maximum number of news to be scraped |
| sleep | 1.0 | Sleep time for each news |
| verbose | False, store_true | If True use verbose mode |

만일 2018년 7월 1일부터 작성된 자료를 1000개까지 받고 싶다면 다음과 같이 실행코드를 입력해주시면 됩니다.

```
scraping_latest_news.py --begin_date 2018/07/01 --directory ./output --max_num 1000 --sleep 1.0
```
최근 순서대로 크롤링한 파일을 살펴보고 싶을때는 usage.ipynb를 사용하세요.

```
[1 / 50] (January 28, 2019) Reports of “Secret” North Korean Missile Bases: Much Ado about Not Much
[2 / 50] (January 23, 2019) Inspector O and the New Cat
[3 / 50] (January 18, 2019) Why is Kim Yong Chol Still Pyongyang’s Choice for US-DPRK Relations?
[4 / 50] (January 18, 2019) Advancing Peace and Security on the Korean Peninsula: The Case for Koreanization
[5 / 50] (January 28, 2019) Reports of “Secret” North Korean Missile Bases: Much Ado about Not Much
[6 / 50] (January 23, 2019) Inspector O and the New Cat
[7 / 50] (January 18, 2019) Why is Kim Yong Chol Still Pyongyang’s Choice for US-DPRK Relations?
[8 / 50] (January 18, 2019) Advancing Peace and Security on the Korean Peninsula: The Case for Koreanization
[9 / 50] (January 16, 2019) Beach Watch: North Korea’s Wonsan Gets a Boost
[10 / 50] (January 9, 2019) North Korea’s Yongbyon Nuclear Facilities: Well Maintained but Showing Limited Operations

Stop scrapping. 32 / 50 news was scrapped
The oldest news has been created after 2018-07-01
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
