import requests
import bs4

url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
contents = requests.get(url)

respon = bs4.BeautifulSoup(contents.text, 'html.parser')
data = respon.find(attrs={'class': 'grid-row list-content'})
titles = data.findAll(attrs={'class': 'media__title'})
images = data.findAll(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])
