from config import *
import requests
import json
import requests
from pprint import pprint
from config import *

# photo_files = ['nasa_pictures/nspct0.png','nasa_pictures/nspct1.png','nasa_pictures/nspct2.png']
def send_media_group(chat_id, image_urls):
    url = f'https://api.telegram.org/bot{token}/sendMediaGroup'
    media = [{'type': 'photo', 'media': url} for url in image_urls]
    payload = {
        'chat_id': chat_id,
        'media': media
    }
    response = requests.post(url, json=payload)
    return response.json() 




    x
def send_media_file(chat_id,token,photo_files,caption):
    media = []
    
    for number,i in enumerate(photo_files):
        Rust = {
            'type':'photo',
            'media': f"attach://random-name-{number}"
        }
        media.append(Rust)
    media[0]["caption"] = caption
    files = {}
    params = {
        "chat_id": chat_id,
        "media": json.dumps(media),
        "contentType": "application/json"
    }   
    for number,r in enumerate(photo_files):
        files[f"random-name-{number}"] = open(r,"rb")
       
    send_text = f'https://api.telegram.org/bot{token}/sendMediaGroup'
    response = requests.post(send_text, params=params, files=files)
    response.raise_for_status()
  

        






# send_media_file(chat_id,token,Photo_files,caption = "あなたのお母さんはクソお尻の息子に犯されました")


