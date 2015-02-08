# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 02:29:41 2015

@author: PRABHUDATTA
"""

username=raw_input('enter an artist you are looking for')
import json,requests,pandas
from pandas import DataFrame,Series
url='http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist='+username+'&api_key=2342c39bedd216dbc94166ab920f099d&format=json'
data=requests.get(url).text
data=json.loads(data)
k=[]
for similar_artist in data['similarartists']['artist']:
    k.append(similar_artist['name'])
df=DataFrame({'Top Artist similar to ' + username :Series(k)}).head(15)
print df
    
