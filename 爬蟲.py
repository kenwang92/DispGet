import requests
import time
from bs4 import BeautifulSoup
import re

print('PPT開爬')

UPurl = requests.get('https://disp.cc/b/Gossiping')
soup = BeautifulSoup(UPurl.text,'html.parser')
UP = soup.find_all('a',{"title":"(PgUp,P)"})
UP = str(UP)
UPlist = re.findall(r'\d+',UP)

while(1):
    url = 'https://disp.cc/b/Gossiping?pn='+UPlist[0]+'&init=0'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    for soup in soup.find_all('span',{"class": "titleColor"}):
        soup = str(soup)
        soup = soup.strip('<span class="titleColor">■</span>')
        print(soup)
    UPurl = requests.get(url)
    soup = BeautifulSoup(UPurl.text,'html.parser')
    UP = soup.find_all('a',{"title":"(PgUp,P)"})
    UP = str(UP)
    UPlist = re.findall(r'\d+',UP)
    time.sleep(5)
