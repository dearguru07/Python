import requests
import pandas
from bs4 import BeautifulSoup

respones=requests.get("https://www.flipkart.com/search?q=iphone+15&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+15%7CMobiles&requestId=6e6547b2-feb2-40f0-bab5-0f0d2743eb29&as-backfill=on")
# print(respones)
soup=BeautifulSoup(respones.content,'html.parser')
# print(soap)
names=soup.find_all('div',class_='KzDlHZ')
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
# print(name)    



prices=soup.find_all('div',class_='Nx9bqj _4b5DiR')
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)
# print(price)


rating=soup.find_all('div',class_='XQDdHH')
rate=[]
for i in rating[0:10]:
    d=i.get_text()
    rate.append(d)
# print(rate)


images=soup.find_all('img',class_='DByuf4')
img=[]
for i in images[0:10]:
    d=i['src']
    img.append(d)
# print(img)

# df=pandas.3