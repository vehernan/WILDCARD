"""
Web Scraping tutorial, https://www.youtube.com/watch?v=ng2o98k983k&t=1380s
using beautiful soup as help;
Web Scraping is used for web indexing, web mining, and data mining.
its the gathering of information fro te web.
"""

from bs4 import BeautifulSoup #to handle all of html processing
import requests #to make http requests
import csv

source = requests.get('http://coreyms.com').text #the website i will be using to scrape

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text 
    print(summary)

    try:
        vid_src = article.find('iframe', class_='youtube-player')['src']

        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()