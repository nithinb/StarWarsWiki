from database.DBOperation import (
    setFavoritePlanetInDB,
    getAllFavoritePlanetsInDB,
    removeFavoritePlanetInDB,

    setFavoriteMovieInDB,
    getAllFavoriteMovieInDB,
    removeFavoriteMovieInDB,

    setFavoriteCharacterInDB,
    getAllFavoriteCharacterInDB,
    removeFavoriteCharacterInDB,

)

from helpers.SwapiHelper import (
    getAllPlanets,
    getSpecificPlanets,

    getAllMovies,
    getSpecificMovies,

    getAllCharacters,
    getSpecificCharacters
)


"""
All helper functions for Planet Data
"""


def setFavoritePlanet(user, PlanetID):
    print("About to set PlanetID: {} as a favorite for the User: {}".format(
        PlanetID, user))
    setFavoritePlanetInDB(user, PlanetID)


def removeFavoritePlanet(user, PlanetID):
    print("About to delete the planet: {} as a favorite from the user: {}".format(
        PlanetID, user))
    removeFavoritePlanetInDB(user, planetID=PlanetID)


def getPlanets(user):
    if(user == None):
        print("About to get all planets")
        rows = getAllPlanets()

    else:
        print("About to get all favorite planets for the user: {}".format(user))
        rows = getAllFavoritePlanetsInDB(user)
        rows = getSpecificPlanets(rows)
    return rows


"""
All helper functions for Movie Data
"""


def setFavoriteMovie(user, MovieID):
    print("About to set MovieID: {} as a favorite for the User: {}".format(
        MovieID, user))
    setFavoriteMovieInDB(user, MovieID)


def removeFavoriteMovie(user, MovieID):
    print("About to delete the movieID: {} as a favorite from the user: {}".format(
        MovieID, user))
    removeFavoriteMovieInDB(user, MovieID)


def getMovies(user):
    if(user == None):
        print("About to get all movies")
        rows = getAllMovies()

    else:
        print("About to get all favorite movies for the user: {}".format(user))
        rows = getAllFavoriteMovieInDB(user)
        rows = getSpecificMovies(rows)

    return rows


"""
All helper functions for Character Data
"""


def setFavoriteCharacter(user, CharacterID):
    print("About to set CharacterID: {} as a favorite for the User: {}".format(
        CharacterID, user))
    setFavoriteCharacterInDB(user, CharacterID)


def removeFavoriteCharacter(user, CharacterID):
    print("About to delete the CharacterID: {} as a favorite from the user: {}".format(
        CharacterID, user))
    removeFavoriteCharacterInDB(user, CharacterID)


def getCharacter(user):
    if(user == None):
        print("About to get all characters")
        rows = getAllCharacters()

    else:
        print("About to get all favorite characters for the user: {}".format(user))
        rows = getAllFavoriteCharacterInDB(user)
        rows = getSpecificCharacters(rows)

    return rows
