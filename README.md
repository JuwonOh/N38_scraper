# N38_scraper

스팀슨 센터(Stimson Center)산하의 연구기관인 38North의 article(https://www.38north.org/articles/)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.
```
python scraping_latest_news.py
```

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

특정한 페이지를 parse하기 위해서는

```python
from Cato_scraper import parse_page
from Cato_scraper import get_allnews_urls

urls = get_allnews_urls(begin_page=1, end_page=3, verbose=True)
for url in urls[:3]:
    json_object = parse_page(url)    
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
