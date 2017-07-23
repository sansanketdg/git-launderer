#!/usr/bin/env python

import logging
import os
import sys
import time

from SleepyDaemons import SleepyDaemon


if __name__ == '__main__':

    action = sys.argv[1]
    logfile = os.path.join(os.getcwd(), "sleepy123.log")
    pidfile = os.path.join(os.getcwd(), "sleepy123.pid")
    print(logfile)
    print(pidfile)
    logfile = '/tmp/sleepy123.log'
    pidfile = '/tmp/sleepy123.pid'

    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    d = SleepyDaemon(pidfile=pidfile)

    if action == "start":
        d.start()

    elif action == "stop":
        d.stop()

    elif action == "restart":
        d.restart()