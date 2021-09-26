import  requests
import json

# url ='https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22CRoNS98B4S2%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A24%7D'

f = open('igData.json',)

data = json.load(f)

users =  data['data']['shortcode_media']['edge_liked_by']['edges']

count = 0
for user in users:
    username = user['node']['username']
    full_name = user['node']['full_name']
    profile_pic_url = user['node']['profile_pic_url']
    count +=1
    print(count)
