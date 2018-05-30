import sys, os.path, time, logging
from typing import List, Any, Union

import pafy
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os, random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFile
import subprocess, signal
import pyinotify


word = 'TE'
exceptions = [word, 'VIJESTI', 'Vijesti', 'BUSINESS AS USUAL', 'SELO MOJE MALO', 'Selo moje malo',
                      'KULTURNI SKALPEL', 'SKOLICA', 'TRANSVERZALA', 'AFTERSHOCK', 'PREGLED', 'RADIOAKTIVITET',
                      'KURIKULUM', 'LUNAROV', 'GRADSKE']


file = r"/media/D/04-PUBLIC/LUKA/NowOnAir.txt"

class ModHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, evt):
        # read NowOnAir
        file = r"/media/D/04-PUBLIC/LUKA/NowOnAir.txt"
        NowOnAir = open(file).readline()
        NowOnAir = NowOnAir[7:]
        # webscrape s vama u eteru
        stranica = 'http://yammat.fm'
        stranica_query = urlopen(stranica)
        juha = BeautifulSoup(stranica_query, 'html.parser')
        upravo_s_vama = juha.find('span', attrs={'class': 'on-air-dj-title'})
        voditelj = upravo_s_vama.text.strip()
        # search youtube based on NowOnAir.txt
        p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        out = out.decode('utf-8')
        for line in out.splitlines():
            if 'vlc' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
        query_string = urllib.parse.urlencode({"search_query": NowOnAir})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        link = ('http://www.youtube.com/watch?v=' + search_results[0])
        videoPafy = pafy.new(link)
        best = videoPafy.getbestvideo()
        videompv = best.url
        subprocess.Popen(['cvlc', '--play-and-exit', videompv])

        #webscrape s vama u eteru
        stranica = 'http://yammat.fm'
        stranica_query = urlopen(stranica)
        juha = BeautifulSoup(stranica_query, 'html.parser')
        upravo_s_vama = juha.find('span', attrs={'class': 'on-air-dj-title'})
        voditelj = upravo_s_vama.text.strip()
        if 'Daniel' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/BILIC'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/BILIC'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Bocca' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/BOCCA'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/BOCCA'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Peh' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/PEH'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/PEH'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Sini' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/SVEC'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/SVEC'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Balen' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/BALEN'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/BALEN'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Ivona' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/IVONA'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/IVONA'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Zdravko' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/MAMIC'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/MAMIC'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Milic' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/MILIC'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/MILIC'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Deutsch' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/SMS'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/SMS'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Vazdar' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/VAZDAR'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/VAZDAR'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        elif 'Ricov' in voditelj:
            path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/VAZDAR'
            os.chdir(path)
            fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/RICOV'))
            im=Image.open(fotka)
            im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        for x in exceptions:
            if x in NowOnAir:
                path ='/home/videostream/PycharmProjects/VisualRadio/images/photos/NOVINARI'
                os.chdir(path)
                fotka = random.choice(os.listdir('/home/videostream/PycharmProjects/VisualRadio/images/photos/NOVINARI'))
                im=Image.open(fotka)
                im.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        #webscrape s vama u eteru
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        fotka = Image.open('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        draw = ImageDraw.Draw(fotka)
        font = ImageFont.truetype('/home/videostream/PycharmProjects/VisualRadio/font/framd.ttf', 66)
        if 'Daniel' in voditelj:
            text = ('S vama su Daniel Bilić i Lucija Čeč')
        else:
            text = 'S vama je ' + voditelj
        draw.text((100, 400),text,(255,255,255),font=font)
        draw = ImageDraw.Draw(fotka)
        fotka.save('/home/videostream/PycharmProjects/VisualRadio/images/photos/fotka.png')
        print(voditelj)


handler = ModHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(file, pyinotify.IN_MODIFY)
notifier.loop()
