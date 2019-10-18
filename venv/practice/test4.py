import json
from urllib.request import urlopen

with urlopen("http://citibikenyc.com/stations/json") as response:
    source =  response.read()

data = json.loads(source)

print (json.dumps(data, indent = 2))
#print(len(data['stationBeanList']))

#for item in data['stationBeanList']:
   # print(item)
 #   name = item['stationName']
  #  docks = item['totalDocks']
   # print(name, docks)

