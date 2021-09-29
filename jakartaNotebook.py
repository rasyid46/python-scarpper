import requests
import bs4
session = requests.session()
import json
import  glob
import  pandas as pd
def get_url():
    res = session.get('https://www.jakartanotebook.com/pc-and-laptop')
    # soup = BeautifulStoneSoup(res.text, 'html5lib')
    response  = bs4.BeautifulSoup(res.content,'html.parser')
    datas = response.find(attrs={'class' : 'product-list-wrapper'})
    contens = datas.find_all(attrs={'class':'product-list'})

    dataCollect = []
    for conten in contens:
        price =conten.find(attrs={'class':'product-list__price'}).text
        link = conten.find(attrs={'class': 'product-list__img'}).find('a')
        url  = link['href']
        title =link['title']
        img = link.find('img')['src']
        dataCollect = {
            'price' : price,
            'url' : url,
            'title' : title,
            'img' : img
        }
        with open('./result/{}.json'.format(url.replace('https://www.jakartanotebook.com/','')),'w') as outfile:
            json.dump(dataCollect,outfile)

# .format(url.replace('https://www.jakartanotebook.com/','')),


def get_detail():
    print('getting detail')


def create_csv():

    files = sorted(glob.glob('./result/*.json'))
    datas = []
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            datas.append(data)

    print('datas',datas)
    df = pd.DataFrame(datas)
    df.to_csv('result.csv',index=False)


def run():
    # get_url()
    # get_detail()
    create_csv()


if __name__ == '__main__':
    run()
