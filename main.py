from bs4 import BeautifulSoup
import requests
import json

url = 'https://en.wikipedia.org/wiki/List_of_cities_and_towns_in_India_by_population'
r = requests.get(url)
data = r.text

soup = BeautifulSoup(data)

cities = []
classes = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6'}

for table in soup.findAll('table', {"class": "wikitable sortable"}):
    for row in table.findAll("tr"):
        cells = row.findAll("td")
        a = []
        for x in cells:

            if x.string is None:
                try:
                    a.append(x.a.string)
                except:
                    a.append(x.string)
            else:
                a.append(x.string)
        q = {}
        if len(a) is not 0:
            q['name'] = str(a[0])
            q['state'] = str(a[1])
            if a[4] is None:
                q['class'] = '6'
            else:
                q['class'] = classes[str(a[4]).split(" ")[1]]

            cities.append(q)
            #print "==========================="

with open('cities.json', 'w') as fp:
    json.dump(cities, fp, indent=4)
