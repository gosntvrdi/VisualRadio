import os.path
from subprocess import call
import os, random
from PIL import Image

def artwork():
    dirname = os.path.dirname(__file__)
    exceptions = ['TE', 'VIJESTI', 'Vijesti', 'BUSINESS AS USUAL', 'SELO MOJE MALO', 'Selo moje malo',
                  'KULTURNI SKALPEL', 'SKOLICA', 'TRANSVERZALA', 'AFTERSHOCK', 'PREGLED', 'RADIOAKTIVITET',
                  'KURIKULUM', 'LUNAROV', 'GRADSKE', 'BREAKOUT']

    file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
    NowOnAir = open(file).readline()
    NowOnAir = NowOnAir[7:]
    NowOnAirException = open(file).readline()
    NowOnAirException = NowOnAirException.split()
    if any(x in NowOnAirException for x in exceptions):
        print('exception')
        path = os.path.join(dirname, 'images/photos/NOVINARI')
        os.chdir(path)
        fotka = random.choice(os.listdir(path))
        try:
            im = Image.open(fotka)
        except:
            im = Image.open('images/NOVINARI/yammat studio_02.jpg')
        im.save(os.path.join(dirname, 'images/fotka.png'))
    else:
        call(['sacad', '-d', '-vdebug', NowOnAir, '', '1920', 'images/fotka.png'])



