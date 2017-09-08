import json
import urllib.request, urllib.parse

service_url = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('input address: ')
    if len(address) < 1:
        break
    url = service_url + urllib.parse.urlencode({
            'address' : address
        })
    con = urllib.request.urlopen(url)
    data = con.read().decode()
    try:
        res = json.loads(data)
    except:
        print('error in loading json')
    place_id = res['results'][0]['place_id']
    print('Place id: %s' %place_id)
