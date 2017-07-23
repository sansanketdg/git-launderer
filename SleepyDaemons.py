import os
import time

from daemons.prefab import run

class SleepyDaemon(run.RunDaemon):

    def run(self):

        while True:
            logfile = '/tmp/sleepy123.log'
            f = open(logfile, "a")
            f.write("I am working after every 10 sec.\n")
            f.close()
            time.sleep(10)