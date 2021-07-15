import bs4
import requests


def detikPopuler():
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    contents = requests.get(url)
    respon = bs4.BeautifulSoup(contents.text, 'html.parser')
    data = respon.find(attrs={'class': 'grid-row list-content'})
    # titles = data.findAll(attrs={'class': 'media__title'})
    images = data.findAll(attrs={'class': 'media__image'})
    return images

def kompasHeadline():
    url = 'https://www.kompas.com/'
    contents = requests.get(url)
    respon = bs4.BeautifulSoup(contents.text, 'html.parser')
    data = respon.find(attrs={'class': 'headline ga--headline clearfix'})
    headlines = data.findAll(attrs={'class': 'headline__big__item'})
    return headlines