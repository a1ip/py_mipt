# -*- coding: utf-8 -*-
import requests
import json
from time import sleep
from token import token

# https://devman.org/qna/63/kak-poluchit-token-polzovatelja-dlja-vkontakte/
# https://oauth.vk.com/blank.html#access_token=<token>&expires_in=86400&user_id=13010236&state=123456
owner_id = -51126445
v = '5.126'

# https://vk.com/dev/wall.get?params[owner_id]=-51126445&params[offset]=1&params[count]=1&params[filter]=owner&params[extended]=1&params[v]=5.84
#params = {'access_token': token, 'owner_id': owner_id_group, 'offset': 1, 'count': 1, 'v': '5.126'}
#data = requests.get('https://api.vk.com/method/wall.get', params=params).json()
#print(data)

#count = 9524
#print(list(range(96)))

# https://vk.com/dev/likes.getList?params[type]=post&params[owner_id]=-51126445&params[item_id]=65731&params[filter]=likes&params[extended]=1&params[count]=1000&params[skip_own]=0&params[v]=5.126
# [type]=post&params[owner_id]=-51126445&params[item_id]=65731&params[filter]=likes&params[extended]=0&params[count]=1000&params[skip_own]=0&params[v]=5.126
#params = {'access_token': token, 'type': 'post', 'item_id': 65731, 'owner_id': owner_id, 'filter': 'likes', 'count': 1000, 'v': v}
#data = requests.get('https://api.vk.com/method/likes.getList', params=params).json()
#print(data)

all_posts = []

for offset in range(96):
    offset *= 100
    params = {'access_token': token, 'owner_id': owner_id, 'offset': offset, 'count': 100, 'v': v}
    data_wall = requests.get('https://api.vk.com/method/wall.get', params=params).json()
    sleep(2)
    print('\n\n\n', offset)
    #print(data_wall['response']['items'][1])
    for ix, item in enumerate(data_wall['response']['items']):
        print(item['id'])
        params = {'access_token': token, 'type': 'post', 'item_id': item['id'], 'owner_id': owner_id, 'filter': 'likes', 'count': 1000, 'v': v}
        likes = requests.get('https://api.vk.com/method/likes.getList', params=params).json()
        #print(likes['response']['items'])
        item['likes']['users_likes'] = likes['response']['items']
        all_posts.append(item)
        if not ix%10:
            sleep(1)
        #break
    #break

with open('posts.json', 'w') as f:
    json.dump(all_posts, f)