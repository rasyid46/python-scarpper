import requests
url ='http://www.floatrates.com/daily/idr.json'
source = requests.get(url)
json_data = source.json()

for data in json_data.values():
    print(data['name'])