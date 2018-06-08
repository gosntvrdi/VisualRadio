from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, random
from PIL import Image



def voditelj():
    dirname = os.path.dirname(__file__)
    stranica = 'http://yammat.fm'
    stranica_query = urlopen(stranica)
    juha = BeautifulSoup(stranica_query, 'html.parser')
    upravoSVama = juha.find('span', attrs={'class': 'on-air-dj-title'})
    voditelj = upravoSVama.text.strip()
    path = os.path.join(dirname, 'images/photos' + '/' + voditelj)
    os.chdir(path)
    fotka = random.choice(os.listdir(path))
    im = Image.open(fotka)
    im.save(os.path.join(dirname, 'images/fotka.png'))
    if voditelj == 'Daniel Bilić':
        text = ('S vama su Daniel Bilić i Lucija Čeč')
    elif voditelj == 'Švec i Peh':
        text = ('S vama su Švec i Peh')
    else:
        text = 'S vama je ' + voditelj
    upravoSVamaTekst = open((os.path.join(dirname, 'upravoSVama.txt')), 'w')
    upravoSVamaTekst.write(text)
    print (voditelj)

