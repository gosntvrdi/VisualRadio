import os.path
import pafy
import urllib.request
import urllib.parse
import re
import os
import subprocess, signal

dirname = os.path.dirname(__file__)


def player():
    file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
    NowOnAir = open(file).readline()
    NowOnAir = NowOnAir[7:]
    NowOnAirOBS = open((os.path.join(dirname, 'NowOnAirOBS.txt')), 'w')
    NowOnAirOBS.write(NowOnAir)
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
    print(best.resolution)
    subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', videompv])
