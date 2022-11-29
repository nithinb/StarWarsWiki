from database.initDB import setupDB
from webserver import setupServer

from helpers.janitor import runJanitor, initPeriodicDBCleaner


def main():
    setupDB()
    initPeriodicDBCleaner()
    setupServer()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        runJanitor()
