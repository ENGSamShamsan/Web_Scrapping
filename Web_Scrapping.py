# Web_Scrapping

# Sam Shamsan, Saturday, Aug 11, 2018
# Platfrom imported : requests, lxml and BeautifulSoup + html5lib
import requests
import lxml
from bs4 import BeautifulSoup
''' intro'''
'''This is a quick WORKING snipit for Web Scraping
    It featch the html page content and print it
    '''
# Get the linke to the webpage you want to scrap
http = requests.get("https://abc7news.com/")
# Soup out the content using lxml schema and beautifulSoup library
soup = BeautifulSoup(http.content, 'lxml')
# You can print the soup now
#print(soup)
# Find out the content attirbute inside the page
main_news= soup.find('meta', itemprop='name')['content']
# You can print the result of you search
#print(main_news)
# Now you can parse
main_news= main_news.lower().split()

print(type(main_news))
print(main_news)

#meta itemprop="name"
