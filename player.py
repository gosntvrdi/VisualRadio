import os.path
import pafy
import urllib.request
import urllib.parse
import re
import subprocess, signal
from subprocess import call
from voditelj import voditelj
import os, random
from PIL import Image
import pyautogui
import time
from songDB import songDB

def animiraniLogo():
    subprocess.call(["xdotool", "windowactivate", "16777221"])
    pyautogui.hotkey('alt', '1')
    time.sleep(14)
    subprocess.call(["xdotool", "windowactivate", "16777221"])
    pyautogui.hotkey('alt', '2')


def player():
    dirname = os.path.dirname(__file__)
    word = ['ATE']
    reklame = ['REKLAME']
    exceptions = ['VIJESTI', 'Vijesti', 'BUSINESS AS USUAL', 'SELO MOJE MALO', 'Selo moje malo',
                  'KULTURNI SKALPEL', 'SKOLICA', 'TRANSVERZALA', 'AFTERSHOCK', 'PREGLED', 'RADIOAKTIVITET', 'KURIKULUM',
                  'LUNAROV', 'GRADSKE', 'JNGL', '041', 'TJEDNI']

    file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
    file2 = os.path.join(dirname, 'NowOnAirOBS.txt')
    image = os.path.join(dirname, 'images/fotka.png')
    imageReklame = os.path.join(dirname, 'images/reklame.jpg')
    NowOnAir = open(file, encoding='utf-8').readline()
    NowOnAir = NowOnAir[7:]
    print(NowOnAir)
    with open(file2, 'w') as f:
        f.write(NowOnAir)
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode('utf-8')
    for line in out.splitlines():
        if 'vlc' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)
    if any(x in NowOnAir for x in exceptions):
        print('Emisija, loadam fotku')
        path = os.path.join(dirname, 'images/photos/NOVINARI')
        os.chdir(path)
        fotka = random.choice(os.listdir(path))
        try:
            im = Image.open(fotka)
        except:
            im = Image.open('images/NOVINARI/yammat studio_02.jpg')
        im.save(os.path.join(dirname, 'images/fotka.png'))
        subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', image])

    elif any(x in NowOnAir for x in word):
        with open(file2, 'w') as f:
            f.write(' ')
        print('DJTalk, palim kameru')
        voditelj()
        subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title',
                          'rtsp://admin:Yammat.2016@192.168.150.99:554/Streaming/Channels/301'])

    elif any(x in NowOnAir for x in reklame):
        print('Reklame')
        subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', imageReklame])

    else:
        query_string = urllib.parse.urlencode({"search_query": NowOnAir})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        try:
            link = ('http://www.youtube.com/watch?v=' + search_results[0])
        except IndexError:
            link = ('https://www.youtube.com/watch?v=l6A4qnAX5Gw')
        try:
            videoPafy = pafy.new(link)
        except (IndexError, OSError) as e:
            videoPafy = pafy.new('https://www.youtube.com/watch?v=l6A4qnAX5Gw')

        best = videoPafy.getbestvideo()
        if all(i >= 480 for i in best.dimensions) and \
                'TunesToTube' and 'HRT' not in videoPafy.description:
            try:
                videompv = best.url
            except AttributeError:
            subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', videompv])
        else:
            call(['sacad', NowOnAir, '', '1920', '/home/videostream/PycharmProjects/VisualRadio/images/fotka.png'])
            subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', image])
        animiraniLogo()
    songDB()

