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
        s = str(i['name']).split('_')
        name.append([i['name'], s[1], s[3].replace('.mp4', '')])
    name.sort(reverse=True)

    return name
