from player import player
from voditelj import voditelj
import pyinotify
import os

dirname = os.path.dirname(__file__)
file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')

class ModHandler(pyinotify.ProcessEvent):
    def process_IN_CLOSE_WRITE(self, evt):
        player()
        voditelj()
        print('in close_Write')


handler = ModHandler()
wm = pyinotify.WatchManager()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(file, pyinotify.IN_CLOSE_WRITE)
notifier.loop()
