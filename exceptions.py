import subprocess, signal
import os


def exception() -> object:
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, 'NowOnAir/NowOnAir.txt')
    word = 'TE'
    exceptions = [word, 'VIJESTI', 'Vijesti', 'BUSINESS AS USUAL', 'SELO MOJE MALO', 'Selo moje malo',
                  'KULTURNI SKALPEL', 'SKOLICA', 'TRANSVERZALA', 'AFTERSHOCK', 'PREGLED', 'RADIOAKTIVITET',
                  'KURIKULUM', 'LUNAROV', 'GRADSKE']
    NowOnAir = open(file).readline()
    NowOnAir = [NowOnAir[7:]]
    for x in NowOnAir:
        if x in exceptions:
            print ('exception ' + x)
            p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
            out, err = p.communicate()
            out = out.decode('utf-8')
            for line in out.splitlines():
                if 'vlc' in line:
                    pid = int(line.split(None, 1)[0])
                    os.kill(pid, signal.SIGKILL)
        else:
            print ('not in exception')

exception()