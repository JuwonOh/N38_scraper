import re
import time
from .utils import get_soup

def get_latest_allnews(last_date, sleep=1.0):
    """
    Artuments
    ---------
    last_date : Date
    sleep : float
        Sleep time. Default 1.0 sec
    """

    raise NotImplemented

patterns = [
    re.compile('https://www.38north.org/[\w]+')]
url_base = 'https://www.38north.org/articles/page/{}/'

def get_allnews_urls(begin_page=1, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_base.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'article__title')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    return links_all

def get_last_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://www.38north.org/articles/page/266/'
    """

    def is_last_link(link):
        return 'pager__link--last' in link.attrs['class']

    def parse(href):
        return int(href.split('page=')[-1])

    last_page = -1
    url = 'https://www.38north.org/articles/'
    soup = get_soup(url)
    for link in soup.select('a[class^=pager__link pager__link--last]'):
        if is_last_link(link):
            last_page = parse(link.attrs['href'])
    return last_page
