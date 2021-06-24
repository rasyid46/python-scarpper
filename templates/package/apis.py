import requests
import bs4
def idrRates():
    url = 'http://www.floatrates.com/daily/idr.json'
    source = requests.get(url)
    json_data = source.json()
    return json_data.values()

def detikPopuler():
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    contents = requests.get(url)
    respon = bs4.BeautifulSoup(contents.text, 'html.parser')
    data = respon.find(attrs={'class': 'grid-row list-content'})
    # titles = data.findAll(attrs={'class': 'media__title'})
    images = data.findAll(attrs={'class': 'media__image'})
    return images
