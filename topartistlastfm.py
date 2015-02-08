#Top_Artist_listeners_Wise
import json,requests,pandas
from pandas import DataFrame,Series
url='http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=2342c39bedd216dbc94166ab920f099d&format=json'
data=requests.get(url).text
data=json.loads(data)
a=[]
b=[]
c=[]
d=[]
for item in data['artists']['artist']:
    a.append(item['name'])
    b.append(item['playcount'])
    c.append(item['listeners'])
df=DataFrame({'ArtistName': Series(a),'PlayCount': Series(b),'listeners':Series(c)})
print df
	

	
