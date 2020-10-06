import requests
from lxml import html

url_post = 'https://habr.com/ru/post/110078/'
page = requests.get(url_post)
tree = html.fromstring(page.content)

title = tree.xpath('//title')
print(title[0].text)

content_lsa = tree.xpath('//div[@id="post-content-body"]')
post_lsa = content_lsa[0].text_content()
#print(content_lsa[0].text_content())


url_top_weekly = 'https://habr.com/ru/top/weekly/'
page = requests.get(url_top_weekly)
tree = html.fromstring(page.content)

title = tree.xpath('//title')
print(title[0].text)

content = tree.xpath('//a[@class="post__title_link"]/@href')
print(content)



print('-'*10, 'NLP', '-'*10)

from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

#print('Load stopwords')
#import nltk
#nltk.download('stopwords')

stemmer = SnowballStemmer("russian")
russian_stopwords = stopwords.words("russian")
#print(post_lsa)
print(' '.join([stemmer.stem(word) for word in post_lsa.split() if word not in russian_stopwords]))
