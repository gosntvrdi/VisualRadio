import mysql.connector as mariadb
import os.path
import subprocess

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
NowOnAir = open(file, encoding='utf-8').readline()
NowOnAir = NowOnAir[7:]
conn = mariadb.connect(host='192.168.150.251', user='videostream', database='songsDB')
cursor = conn.cursor(buffered=True)
cursor.execute("""SELECT youtubeLink FROM songsDB WHERE songName = ' ' + '%s' """), (NowOnAir)
#cursor.execute("""SELECT youtubeLink FROM songsDB WHERE songName = 'Disclosure - Ultimatum' """)
conn.commit()
youtubeLink = cursor.fetchone()
youtubeLink = ' '.join(map(str, (youtubeLink)))
print (youtubeLink)
vlc_path = 'C:/Program Files/VideoLAN/VLC/vlc.exe'
subprocess.call([vlc_path, youtubeLink, '--play-and-exit', '--qt-start-minimized'], shell=False)

