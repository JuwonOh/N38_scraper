from .utils import get_soup
from .utils import now
from dateutil.parser import parse

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h1', class_= 'page-header').text
        time = soup.find('ul', class_='post__meta list-inline').find('li', class_='meta--date').text
        phrases = soup.find('div', class_='content').find_all('p')
        content = '\n'.join([p.text.strip() for p in phrases])
        author = soup.find('a', class_= 'author url fn').text

        json_object = {
            'title' : title,
            'time' : parse(time),
            'author' :author,
            'content' : content,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
