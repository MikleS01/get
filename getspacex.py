import requests 
from pprint import pprint 
import random
def getspacex():
    launches_w_photos = []    
    spacex = []
    URL = "https://api.spacexdata.com/v5/launches"
    response = requests.get(URL)
    response.raise_for_status()
   
    for i in (response.json()):
        if i['links']['flickr']['original'] != []:
            launches_w_photos.append(i['links']['flickr']['original'])
        
    
    
    for number,i in enumerate(random.choice(launches_w_photos)):
        responsedw = requests.get(i)
        responsedw.raise_for_status()      
        with open(f'spxpictr/spxpictr{number}.png','wb') as file:
            file.write(responsedw.content)
      

