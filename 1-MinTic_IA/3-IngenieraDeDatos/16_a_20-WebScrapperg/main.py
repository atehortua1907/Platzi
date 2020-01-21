import argparse
import logging
logging.basicConfig(level=logging.INFO)
import news_page_objects as news 
from common import config
import re #regex
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

logger = logging.getLogger(__name__)
is_well_formed_url = re.compile(r'^https?://.+/.+$') #https://example.com/hello
is_root_path = re.compile(r'^/.+$') #/some-text

def _news_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']
    
    logging.info(f'Beginning scraper for {host}') #logging es una forma de print
    homepage = news.HomePage(news_site_uid, host)

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site_uid, host, link)

        if article:
            logger.info('Article fetched!!')
            articles.append(article)
            print(article.title)
    
    print(len(articles))

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