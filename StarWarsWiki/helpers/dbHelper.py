import sqlite3 as sl

databaseConnection = None


def healthCheck(databaseConnection):
    if(databaseConnection == None):
        return False

    healthCheckQuery = """
        SELECT 1;
    """
    try:
        rows = databaseConnection.execute(healthCheckQuery).fetchall()
        if(len(rows) > 0):
            return True
        return False
    except:
        return False


def connectToDBIfRequired(databaseConnection):
    if(databaseConnection != None and healthCheck(databaseConnection)):
        return databaseConnection

    try:
        databaseConnection = sl.connect('StarWarsWiki.db')
        return databaseConnection
    except Exception as e:
        print("Error while connecting to the DB: ", e)
        return False


def executeQuery(query):

    global databaseConnection
    databaseConnection = connectToDBIfRequired(databaseConnection)

    if(databaseConnection == False):
        print("Cannot execute query")
        return

    print("About to execute the query: ", query)
    rows = databaseConnection.execute(query).fetchall()
    databaseConnection.commit()
    return rows
