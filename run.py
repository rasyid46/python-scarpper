

from flask import Flask, render_template

from templates.package.apis import idrRates, detikPopuler
from scarpData.news import kompasHeadline


app =Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')
@app.route('/populer')
def detik_populer():
    images = detikPopuler()
    return render_template('detikscraper.html', images=images)
@app.route('/rates')
def idr_rates():
    datas = idrRates()
    return render_template('idrrates.html', datas=datas)
@app.route('/kompas')
def kompas_headline():
    headlines = kompasHeadline()
    return  render_template('kompas.html',headlines= headlines)

if __name__=='__main__':
    app.run(debug=True)

