import json
import time

from helpers.dbHelper import executeQuery


CACHEEXPIRY = 3600


"""
All database operations related to Planet
"""


def setFavoritePlanetInDB(user, planetID):
    query = """
        INSERT INTO PlanetFavorites (userID, PlanetID)
        VALUES ({}, {})
        RETURNING *;
    """.format(user, planetID)

    executeQuery(query)


def getAllFavoritePlanetsInDB(user):
    query = """
        SELECT userID, PlanetID
        FROM PlanetFavorites
        WHERE userID={};
    """.format(user)

    rows = executeQuery(query)
    return rows


def removeFavoritePlanetInDB(user, planetID):
    query = """
        DELETE FROM PlanetFavorites
        WHERE userID={} and PlanetID={};
    """.format(user, planetID)

    executeQuery(query)


"""
All database operations related to Movies
"""


def setFavoriteMovieInDB(user, MovieID):
    query = """
        INSERT INTO MovieFavorites (userID, MovieID)
        VALUES ({}, {})
        RETURNING *;
    """.format(user, MovieID)

    executeQuery(query)


def getAllFavoriteMovieInDB(user):
    query = """
        SELECT userID, MovieID
        FROM MovieFavorites
        WHERE userID={};
    """.format(user)

    rows = executeQuery(query)
    return rows


def removeFavoriteMovieInDB(user, MovieID):
    query = """
        DELETE FROM MovieFavorites
        WHERE userID={} and MovieID={};
    """.format(user, MovieID)

    executeQuery(query)


"""
All database operations reldated to Character
"""


def setFavoriteCharacterInDB(user, CharacterID):
    query = """
        INSERT INTO CharacterFavorites (userID, CharacterID)
        VALUES ({}, {})
        RETURNING *;
    """.format(user, CharacterID)

    executeQuery(query)


def getAllFavoriteCharacterInDB(user):
    query = """
        SELECT userID, CharacterID
        FROM CharacterFavorites
        WHERE userID={};
    """.format(user)

    rows = executeQuery(query)
    return rows


def removeFavoriteCharacterInDB(user, CharacterID):
    query = """
        DELETE FROM CharacterFavorites
        WHERE userID={} and CharacterID={};
    """.format(user, CharacterID)

    executeQuery(query)


"""
Cache data in Database
"""


def checkURLCache(url):

    timestamp = int(time.time()) - CACHEEXPIRY
    query = """
        SELECT data, next
        FROM URLCache
        WHERE url='{}' AND createdat>{}
        order by createdat DESC
        LIMIT 1;
    """.format(url, timestamp)

    rows = executeQuery(query)
    if(len(rows) == 0):
        return None, None
    data, next = rows[0]
    data = json.loads(data)
    if(next == 'None'):
        next = None
    return data, next


def cacheURLData(url, data, nextURL):
    currentTimestamp = int(time.time())
    dataString = json.dumps(data)
    dataString.replace("'", "\'")
    dataString.replace('"', '\"')

    query = """
        INSERT INTO URLCache (url, data, next, createdAt)
        VALUES ('{}', '{}', '{}', {});
    """.format(url, dataString, nextURL, currentTimestamp)

    executeQuery(query)


def cleanupCacheTable():
    expiredRows = int(time.time()) - CACHEEXPIRY
    query = """
        DELETE FROM URLCache
        WHERE createdat < {};
    """.format(expiredRows)

    executeQuery(query)
