from getnasa import getnasa
from getspacex import getspacex
import os
import shutil
from config import * 


def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)

clear_folder(folder_path = "spxpictr")
clear_folder(folder_path = "nasa_pictures")
getspacex()
getnasa(nasatoken)
