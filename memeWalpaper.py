import ctypes
import requests 
from datetime import datetime

url = 'https:' + requests.get('https://dilbert-api.glitch.me/json').json()["image"]

r = requests.get(url, allow_redirects=True)
open('_'.join(str(  datetime.now()).split()).split('.')[0].replace(':' ,'-')  + ".jpg", 'wb').write(r.content)


SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParameters(SPI_SETDESKWALLPAPER, 0, '_'.join(str(  datetime.now()).split()).split('.')[0].replace(':' ,'-')  + ".jpg" , 0)