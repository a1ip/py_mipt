import requests
from lxml import html
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")

url_post = 'https://habr.com/ru/post/110078/'
page = requests.get(url_post)
tree = html.fromstring(page.content)

title = tree.xpath('//title')
title_text = title[0].text
print(title_text)
print([stemmer.stem(word) for word in title_text.split()])

content = tree.xpath('//div[@id="post-content-body"]')
#print(content[0].text_content())


url_top_weekly = 'https://habr.com/ru/top/weekly/'
page = requests.get(url_top_weekly)
tree = html.fromstring(page.content)

title = tree.xpath('//title')
print(title[0].text)

content = tree.xpath('//a[@class="post__title_link"]/@href')
print(content)
