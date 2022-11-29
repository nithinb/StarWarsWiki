from database.DBOperation import cleanupCacheTable

import multiprocessing
import time

thread = None
CLEANUPFREQUENCY = 3600


def runJanitor():
    cleanupCacheTable()
    thread.terminate()
    print("Terminated the process with pid: ", thread.pid)


def periodicDBCleaner():
    try:
        while True:
            time.sleep(CLEANUPFREQUENCY)
            cleanupCacheTable()
    except:
        print("Terminated the periodic cleanup process")


def initPeriodicDBCleaner():
    global thread
    thread = multiprocessing.Process(
        target=periodicDBCleaner
    )
    thread.start()
    print("Starting thread with PID: ", thread.pid)
