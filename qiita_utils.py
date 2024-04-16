import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup

def fetch_trending_articles(url="https://qiita.com/popular-items/feed", max_articles=5):
    articles = []
    
    response = requests.get(url)
    root = ET.fromstring(response.content)

    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}

    for entry in root.findall('atom:entry', namespaces)[:max_articles]:
        link = entry.find('atom:link[@rel="alternate"]', namespaces).attrib['href']
        title = entry.find('atom:title', namespaces).text
        articles.append((link, title))

    return articles

def fetch_article_content(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding

    soup = BeautifulSoup(response.text, 'html.parser')
    article_content = soup.find('div', {'id': 'personal-public-article-body'}).text.strip()
    return article_content
