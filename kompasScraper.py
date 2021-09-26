import requests
import bs4
url = 'https://www.kompas.com/'
contents = requests.get(url)
respon = bs4.BeautifulSoup(contents.text, 'html.parser')
data = respon.find(attrs={'class' : 'headline ga--headline clearfix'})
headlines = data.findAll(attrs={'class' : 'headline__big__item'})
dataCollect = []
for headline in headlines :
    url = headline.find('a')['href']
    img = headline.find('a').find('img')['data-src']
    title = headline.find('a').find('img')['alt']
    item = {
        'url': url,
        'title': title,
        'img': img
    }
    dataCollect.append(item)

print(dataCollect)