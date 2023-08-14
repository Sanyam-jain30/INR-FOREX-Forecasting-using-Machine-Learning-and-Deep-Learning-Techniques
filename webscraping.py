import pandas as pd
from bs4 import BeautifulSoup
import requests
import warnings
import base64
from selenium import webdriver

warnings.filterwarnings('ignore')

dr = webdriver.Chrome()
df = pd.DataFrame(columns=['Date', 'Price', 'Open', 'High', 'Low', 'Volume', 'Chg'])

url = "https://in.investing.com/currencies/usd-inr-historical-data?end_date=1680451891&interval_sec=daily&st_date=1456943400"

dr.get(url)

soup = BeautifulSoup(dr.page_source, "lxml")
section = soup.find('section', attrs={'class': 'js-table-wrapper common-table-comp scroll-view'})
div = section.find('div', attrs={'class': 'common-table-wrapper'})
table = div.find('table')
tbody = table.find('tbody')

for tr in tbody.findAll('tr'):
    list_data = []
    for td in tr.findAll('td'):
        list_data.append(td.find('span').text)
    df.loc[len(df)] = list_data
    
df.head()

df.to_csv("Investing_INR_Rates.csv")
