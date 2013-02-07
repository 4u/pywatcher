import os.path
from subprocess import check_call

def compile(config):
    cdir = os.path.abspath(os.path.dirname(__file__))
    gcin = os.path.join(cdir, 'watcher/bin/watcher')
    cmd = [
        watcher,
        '-c', config
    ]

    print "Running watcher: ", ' '.join(cmd)
    check_call(cmd)
    print "Done"
