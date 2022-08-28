import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.ask.com/web?q=larry%20page&ad=dirN&o=0&ueid=c1b0bd67-7cfb-4b4d-9cda-6d0959805f89')
soup = BeautifulSoup(res.text, 'lxml')
results_title = soup.find_all('div', {'class': 'PartialRelatedSearch-body'})

for titles in results_title:
    print(titles.getText())
