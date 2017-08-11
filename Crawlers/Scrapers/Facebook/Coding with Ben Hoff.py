#Trying to build a python scipt to pull out user information of users based on the profile IDs (Learning from Ben Hoff)

import json
import os
import urllib.request
import base64

url="https://graph.facebook.com/v2.10/me/photos"
facebook_api_key='5e4111fedb9de3c7cd76c7f857fb4119'
base64string=base64.encodebytes

request=urllib.request.Request(url)
request.add_header('Authorization', 'Bearer {}'.format(facebook_api_key))
#request.add_header('access_token',facebook_api_key)

response =urllib.request.urlopen(request)
encoding = response.headers.get_content_charset()
if encoding is None:
    print('encoding None!')
    encoding='utf-8'

data=json.loads(response.read().decode(encoding))
print(data)


#Left at 45:12 as the code started working for BEn Hoff and not for me and will try to figure out why.