import pafy
import os
import subprocess, signal
import re
import urllib.request
import urllib.parse
from scratch import artwork

artwork()
dirname = os.path.dirname(__file__)
file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
with open (file, 'rb') as f:
    NowOnAir = f.read()

NowOnAir = NowOnAir[7:]

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
if all(i >= 720 for i in best.dimensions):
    videompv = best.url
    subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', videompv])
else:
    subprocess.Popen(['cvlc', '--play-and-exit', '--no-video-title', 'images/fotka.png'])
