import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup

import artifact_utils

def fetch_trending_articles(url="https://qiita.com/popular-items/feed", count=5):
    previous_articles = artifact_utils.load_previous_results()

    articles = []
    
    response = requests.get(url)
    root = ET.fromstring(response.content)

    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}

    for entry in root.findall('atom:entry', namespaces)[:10]:
        if len(articles) >= count:
            break
        link = entry.find('atom:link[@rel="alternate"]', namespaces).attrib['href']
        if link not in previous_articles:
            title = entry.find('atom:title', namespaces).text
            articles.append((link, title))

    artifact_utils.save_results(articles)
    return articles

def fetch_article_content(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, 'html.parser')
    article_content = soup.find('div', {'id': 'personal-public-article-body'}).text.strip()
    return article_content[:6000]
