import requests
from pprint import pprint

def getnasa(api_key):
   aceton = []
   URL =  "https://api.nasa.gov/planetary/apod"
   
   params = {  
      "api_key": api_key,
      "count": 3
      }
   
   
   photo_links = []
   #Получить из API ссылку на 10 изображений
   response = requests.get(URL,params = params)
   response.raise_for_status()
   for a in response.json():

      if 'hdurl' in a :
         if 'youtube' not in 'hdurl':
            photo_links.append(a['hdurl'])
            

      else:
         if 'youtube' not in 'url':
            photo_links.append(a['url'])

               
   for number,i in enumerate(photo_links):
      responsedw = requests.get(i)
      responsedw.raise_for_status()      
      with open(f'nasa_pictures/nspct{number}.png', "wb") as file:
        file.write(responsedw.content)
   
   return photo_links   
pprint(getnasa("k8FHszIOyyxH16qEVedh63E4rxMpoOz9V2oF82Xx"))