

from flask import Flask, render_template

from templates.package.apis import idrRates, detikPopuler

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
if __name__=='__main__':
    app.run(debug=True)

