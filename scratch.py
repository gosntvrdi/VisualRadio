from voditelj import voditelj
from player import player
import pyinotify

file = 'NowOnAir/NowOnAir.txt'


def onChange(ev):
    player()

wm = pyinotify.WatchManager()
wm.add_watch(file, pyinotify.IN_CLOSE_WRITE, onChange)
notifier = pyinotify.Notifier(wm)
notifier.loop()