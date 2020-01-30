import argparse
import logging
logging.basicConfig(level=logging.INFO)
import news_page_objects as news 
from common import config
import re #regex
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError
import datetime
import csv

logger = logging.getLogger(__name__)
is_well_formed_url = re.compile(r'^https?://.+/.+$') #https://example.com/hello
is_root_path = re.compile(r'^/.+$') #/some-text

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    
    logging.info(f'Beginning scraper for {host}') #logging es una forma de print
    homepage = news.HomePage(news_site_uid, host)

    articles = []
    listLinks = list(homepage.article_links)
    count = 0
    for link in listLinks[0:30]:
        count += 1
        logger.info(count)
        article = _fetch_article(news_site_uid, host, link)

        if article:
            logger.info('Article fetched!!')
            articles.append(article)
            #break #rompemos el ciclo con el fin de probar

    _save_articles(news_site_uid, articles)
 
def _save_articles(news_site_uid, articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = f'{news_site_uid}_{now}_articles.csv'
    csv_headers = filter(lambda property: not property.startswith('_'), dir(articles[0]))
    with open(out_file_name, mode='w+') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)


def _fetch_article(news_site_uid, host, link):
    logger.info(f'start fetching article at {link}')
    article = None
    try:
        article = news.ArticlePage(news_site_uid, build_link(host, link))
    except (HTTPError, MaxRetryError):
        logger.warning('Error while fetching the article', exc_info=False)

    if article and not article.body:
        logger.warning('Invalid article. There is no body')
        return None
    
    return article

def build_link(host, link):
    if is_well_formed_url.match(link):
        return link
    elif is_root_path.match(link):
        return f'{host}{link}'
    else:
        return '{host}/{uri}'.format(host=host, uri=link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    new_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site',
                         help='The news site that you want to scrape',
                         type=str,
                         choices=new_site_choices)
    
    args = parser.parse_args()
    _news_scraper(args.news_site)