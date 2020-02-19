import json, pprint, requests, sys, time


data = open("card2.json")
url = 'https://lookup.binlist.net/'
data_loaded = json.load(data)

for i in data_loaded:
    card_id = str(i['CreditCard']['CardNumber'])[0:8]
    r = requests.get(url + card_id, headers={'Accept-Version': "3"})
    print(r.url)
    print(r.status_code)
    print(r.text)
    if 200 <= r.status_code <= 299:
        output = r.json()['bank']['name']
    else:
        print(r.status_code)
    time.sleep(10)


