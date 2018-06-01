from player import player
from exceptions import exception
from voditelj import voditelj
import pyinotify

class FileWatcher:
    notifier = None

    def start_watch(self, dir, callback):
        wm = pyinotify.WatchManager()
        self.notifier = pyinotify.Notifier(wm, EventProcessor(callback))
        mask = (pyinotify.IN_CREATE | pyinotify.IN_MODIFY | pyinotify.IN_DELETE
                | pyinotify.IN_DELETE_SELF | pyinotify.IN_MOVED_FROM | pyinotify.IN_CLOSE_WRITE
                | pyinotify.IN_MOVED_TO)
        wdd = wm.add_watch(dir, mask, rec=True)
        while True:
            self.notifier.process_events()
            if self.notifier.check_events():
                self.notifier.read_events()

class EventProcessor(pyinotify.ProcessEvent):
    def __init__(self, callback):
        self.event_callback = callback

    def process_IN_CLOSE_WRITE(self, event):

        player()
        exception()
        voditelj()
        print('in close_Write')

f = FileWatcher()
f.start_watch(r'NowOnAir/NowOnAir.txt/', None)