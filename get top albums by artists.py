#Best_Albums_Artists_LastFm():
name=raw_input('Enter a fuckin artist name man')
import json,requests,pandas
from pandas import DataFrame,Series
url='http://ws.audioscrobbler.com/2.0/?method=artist.gettopalbums&artist='+ name +'&api_key=2342c39bedd216dbc94166ab920f099d&format=json' #Please get your own api keyfrom last.fm/api
data=requests.get(url).text
data=json.loads(data)
a=[]
b=[]
#c=[]
for item in data['topalbums']['album']:
    a.append(item['@attr']['rank'])
    b.append(item['name'])
df=DataFrame({'Rank': Series(a),'Album': Series(b)}).head(10)
print df
	

	
