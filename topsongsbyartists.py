#Best_Albums_Artists_LastFm():
name=raw_input('Enter a fuckin artist name man')
import json,requests, pandas
from pandas import DataFrame,Series
url='http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist='+name+'&api_key=2342c39bedd216dbc94166ab920f099d&format=json'#Please get your own api keyfrom last.fm/api
data=requests.get(url).text #dont use urllib.urlopen(url) for requests api's
data=json.loads(data)
a=[]
b=[]
c=[]
d=[]
for item in data['toptracks']['track']:
    a.append(item['name'])
    b.append(item['@attr']['rank'])
    c.append(item['playcount'])
    d.append(item['duration'])
df=DataFrame({'Top Tracks by '+ name: Series(a),'Rank': Series(b),'PlayCount': Series(c),'Duration of the track': Series(d)}).head(10)
print df
	

	
