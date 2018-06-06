import os.path
import pafy
import urllib.request
import urllib.parse
import re
import os
import subprocess, signal
from artwork import artwork



def player():
    dirname = os.path.dirname(__file__)
    exceptions = ['VIJESTI', 'Vijesti', 'BUSINESS AS USUAL', 'SELO MOJE MALO', 'Selo moje malo',
                  'KULTURNI SKALPEL', 'SKOLICA', 'TRANSVERZALA', 'AFTERSHOCK', 'PREGLED', 'RADIOAKTIVITET',
                  'KURIKULUM', 'LUNAROV', 'GRADSKE', 'BREAKOUT']
    DJTalk = ['TE']
    file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
    with open (file, 'rb') as f:
        NowOnAir = f.read()
    NowOnAir = NowOnAir[7:]
    print (NowOnAir)
    NowOnAirOBS = open((os.path.join(dirname, 'NowOnAirOBS.txt')), 'wb')
    NowOnAirOBS.write(NowOnAir)
    NowOnAirException = open(file, 'rb').readline()
    NowOnAirException = NowOnAir.split()
    print (NowOnAir)
    print (NowOnAirException)
    p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode('utf-8')
    for line in out.splitlines():
        if 'vlc' in line:
            pid = int(line.split(None, 1)[0])
            os.kill(pid, signal.SIGKILL)
    if any(x in NowOnAirException for x in exceptions):
        subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', 'images/fotka.png'])
    elif any(x in NowOnAirException for x in DJTalk):
        print ('DJTalk')
        subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', 'rtsp://admin:Yammat.2016@192.168.150.99:554/Streaming/Channels/301'])
    else:
        query_string = urllib.parse.urlencode({"search_query": NowOnAir})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        try:
            link = ('http://www.youtube.com/watch?v=' + search_results[0])
        except IndexError:
            link = ('https://www.youtube.com/watch?v=l6A4qnAX5Gw')
        videoPafy = pafy.new(link)
        best = videoPafy.getbestvideo()
        print(best)
        if all(i >= 600 for i in best.dimensions):
            videompv = best.url
            subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', videompv])
        else:
            artwork()
            subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', 'images/fotka.png'])


