import json, pprint, requests, sys, time


#with open("card2.json") as f:
#    cards = json.load(f)
#pprint.pprint(cards)

data = open("card2.json")
url = 'https://lookup.binlist.net/'
data_loaded = json.load(data)

for i in data_loaded:
    card_id = str(i['CreditCard']['CardNumber'])[0:8]
    r = requests.get(url + card_id, headers={'Accept-Version': "3"})

time.sleep(2)

if r.status_code >= 200 <= 299:
        pprint.pprint(r.json()['bank']['name'])
else:
        print(r.status_code)