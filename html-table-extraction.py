import csv
from bs4 import BeautifulSoup


import urllib3
response = urllib3.PoolManager().request('GET', 'https://www.auto-decibel-db.com/desktop.html')
html_data = response.data


tree = BeautifulSoup(html_data,"html5lib")
table_tag = tree.select("table")[1]
tab_data = [[item.text for item in row_data.select("th,td")] 
                for row_data in table_tag.select("tr")]


with open('car_db.csv', 'w', encoding="utf8") as f:
    writer = csv.writer(f)
    for row in tab_data:
        writer.writerow(row)
