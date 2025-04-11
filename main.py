from getnasa import getnasa
from tg_bots import send_media_group
from getspacex import getspacex
import os
import shutil
from config import * 
import requests
import random 
from tg_bots import *  


pyti = []
random_sp = ['nasa','spacex']


def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)

clear_folder(folder_path = "spxpictr")
clear_folder(folder_path = "nasa_pictures")

launch_date = 00
nos = random.choice(random_sp)
# print(nos)
if nos == 'nasa':
    getnasa(nasa_token)
    photo_files = os.listdir("nasa_pictures") 
    for i in photo_files:
        pyti.append(f'nasa_pictures/{i}')
    text = 'Картинка дня от Nasa☑'
else:
    getspx = getspacex()
    photo_files =os.listdir("spxpictr")
    for i in photo_files:
        pyti.append(f'spxpictr/{i}')
    text = f" Запуск ракеты SpaceX☑. совершен: {getspx} "

send_media_file(tg_chat_id,tg_token,pyti,text)
# print(photo_files)

