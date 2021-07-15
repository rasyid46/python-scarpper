import requests
import bs4

url = 'https://www.kompas.com/'
contents = requests.get(url)
respon = bs4.BeautifulSoup(contents.text, 'html.parser')
data = respon.find(attrs={'class' : 'headline ga--headline clearfix'})
headlines = data.findAll(attrs={'class' : 'headline__big__item'})


for headline in headlines :
    # print(headline.find('a')['href'])
    print(headline.find('a').find('img'))
    # print(headline.find('a').find('img')['data-src'])
