import firebase_config
import requests
import json


def get_video_data():
    storage = firebase_config.firebase.storage()
    url = storage.get_url(None)
    r = requests.get(url)
    with open('json_file/link.json', 'wb') as f:
        f.write(r.content)

    # Opening JSON file
    f = open('json_file/link.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    name = []
    # Iterating through the json
    # list
    for i in data['items']:
        s1 = str(i).split(': ')
        s2 = s1[1].split('\'')
        name.append(s2[1])
    name.sort(reverse=True)

    data = []

    for n in name:
        d = n.split('_')
        data.append([n, d[1]])

    return data


for n, d in get_video_data():
    print(n, d)
