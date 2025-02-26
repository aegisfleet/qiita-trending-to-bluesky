import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
from typing import Optional

import artifact_utils

def fetch_trending_articles(url: str = "https://qiita.com/popular-items/feed", count: int = 5):
    previous_articles = artifact_utils.load_previous_results()

    articles = []

    response = requests.get(url)
    root = ET.fromstring(response.content)

    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}

    for entry in root.findall('atom:entry', namespaces)[:10]:
        if len(articles) >= count:
            break
        link_element = entry.find('atom:link[@rel="alternate"]', namespaces)
        title_element = entry.find('atom:title', namespaces)

        if link_element is not None and title_element is not None:
            link = link_element.get('href')
            title = title_element.text
            if link is not None and title is not None and link not in previous_articles:
                articles.append((link, title))

    artifact_utils.save_results(articles)
    return articles

def fetch_article_content(url: str) -> Optional[str]:
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, 'html.parser')
    article_body = soup.find('div', {'id': 'personal-public-article-body'})
    if article_body:
        return article_body.text.strip()[:6000]
    return None
