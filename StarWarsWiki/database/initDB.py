from helpers.dbHelper import executeQuery


def dropExistingTables():
    dropTableUsers = """
        DROP TABLE USERS;
    """

    dropTableMovieFavorites = """
        DROP TABLE MovieFavorites;
    """

    dropTablePlanetFavorites = """
        DROP TABLE PlanetFavorites;
    """

    dropTableCharacterFavorites = """
        DROP TABLE CharacterFavorites;
    """

    dropTableURLCache = """
        DROP TABLE URLCache;
    """

    executeQuery(dropTableUsers)
    executeQuery(dropTableMovieFavorites)
    executeQuery(dropTablePlanetFavorites)
    executeQuery(dropTableCharacterFavorites)
    executeQuery(dropTableURLCache)


def initTables():

    createTableUsers = """
        CREATE TABLE IF NOT EXISTS
        Users(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """

    createTableMovieFavorites = """
        CREATE TABLE IF NOT EXISTS
        MovieFavorites(
            userID INTEGER,
            MovieID INTEGER
        )
    """

    createTablePlanetFavorites = """
        CREATE TABLE IF NOT EXISTS
        PlanetFavorites(
            userID INTEGER,
            PlanetID INTEGER
        )
    """

    createTableCharacterFavorites = """
        CREATE TABLE IF NOT EXISTS
        CharacterFavorites(
            userID INTEGER,
            CharacterID INTEGER
        )
    """

    createTableURLCache = """
        CREATE TABLE IF NOT EXISTS
        URLCache(
            url VARCHAR,
            data VARCHAR,
            next VARCHAR,
            createdat INTEGER DESC
        )
    """

    executeQuery(createTableUsers)
    executeQuery(createTableMovieFavorites)
    executeQuery(createTablePlanetFavorites)
    executeQuery(createTableCharacterFavorites)
    executeQuery(createTableURLCache)


def initIndexes():
    createUniqueIndex_PlanetFavorites_userID_PlanetID = """
        CREATE UNIQUE INDEX IF NOT EXISTS 
        idx_planetfavorites_userid_planetid 
        ON PlanetFavorites(userID, PlanetID);
    """

    createIndex_PlanetFavorites_userID = """
        CREATE INDEX IF NOT EXISTS 
        idx_planetfavorites_userid 
        ON PlanetFavorites(userID);
    """

    createUniqueIndex_MovieFavorites_userID_PlanetID = """
        CREATE UNIQUE INDEX IF NOT EXISTS 
        idx_MovieFavorites_userid_movieid 
        ON MovieFavorites(userID, MovieID);
    """

    createIndex_MovieFavorites_userID = """
        CREATE INDEX IF NOT EXISTS 
        idx_MovieFavorites_userid 
        ON MovieFavorites(userID);
    """

    createUniqueIndex_CharacterFavorites_userID_PlanetID = """
        CREATE UNIQUE INDEX IF NOT EXISTS 
        idx_CharacterFavorites_userid_characterid 
        ON CharacterFavorites(userID, CharacterID);
    """

    createIndex_CharacterFavorites_userID = """
        CREATE INDEX IF NOT EXISTS 
        idx_CharacterFavorites_userid 
        ON CharacterFavorites(userID);
    """

    createIndex_URLCache_URLCreatedAt = """
        CREATE INDEX IF NOT EXISTS
        idx_URLCache_url_createdat
        ON URLCache(url, createdat);
    """

    createIndex_URLCache_URL = """
        CREATE INDEX IF NOT EXISTS
        idx_URLCache_url
        ON URLCache(url)
    """

    executeQuery(createUniqueIndex_PlanetFavorites_userID_PlanetID)
    executeQuery(createIndex_PlanetFavorites_userID)
    executeQuery(createUniqueIndex_MovieFavorites_userID_PlanetID)
    executeQuery(createIndex_MovieFavorites_userID)
    executeQuery(createUniqueIndex_CharacterFavorites_userID_PlanetID)
    executeQuery(createIndex_CharacterFavorites_userID)
    executeQuery(createIndex_URLCache_URL)


def setupDB():
    # dropExistingTables()
    initTables()
    initIndexes()
