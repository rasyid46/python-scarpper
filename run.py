import requests
import bs4

from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/populer')
def detik_populer():
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    contents = requests.get(url)

    respon = bs4.BeautifulSoup(contents.text, 'html.parser')
    data = respon.find(attrs={'class': 'grid-row list-content'})
    titles = data.findAll(attrs={'class': 'media__title'})
    images = data.findAll(attrs={'class': 'media__image'})
    return render_template('index.html', images=images)
if __name__=='__main__':
    app.run(debug=True)

