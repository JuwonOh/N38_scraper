# N38_scraper

스팀슨 센터(Stimson Center)산하의 연구기관인 38North()의 article(https://www.38north.org/articles/)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

## 주의사항

init부분이 제대로 작동하지 않아, usage부분에서 parser가 직접 import되지 않습니다. 가능한 빨리 수정할 예정입니다. 

하지만 직접적인 크롤러의 작동에는 큰 이상 없습니다.
