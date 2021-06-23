import bs4
import requests

url: str = 'http://www.jadwalsholat.pkpu.or.id/?id=14'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
sholat = {}
i = 0
for d in data[0]:
    if i == 1:
        sholat['subuh'] = d.get_text()
    elif i == 2:
        sholat['zuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['magrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1
print(sholat)
