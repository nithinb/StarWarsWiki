import requests
from database.DBOperation import (
    checkURLCache,
    cacheURLData
)


"""
All methods for Planets
"""


def filterPlanetAttributeList(data, isFavorite=False):
    filteredData = []
    for row in data:
        print(row)
        newRow = {}
        newRow["name"] = row.get("name")
        newRow["created"] = row.get("created")
        newRow["updated"] = row.get("edited")
        newRow["url"] = row.get("url")
        newRow["isFavorite"] = isFavorite
        filteredData.append(newRow)
    return filteredData


def getAllPlanets():
    rows = []
    url = "https://swapi.dev/api/planets/"
    while(url):
        data, next = checkURLCache(url)
        if(not data):
            result = requests.get(url).json()
            data = result["results"]
            data = filterPlanetAttributeList(data)
            next = result['next']
            print(next)
            cacheURLData(url, data, next)

        rows.extend(data)
        url = next
    return rows


def getSpecificPlanets(planetIDList):
    baseUrl = "https://swapi.dev/api/planets/{}/"
    rows = []

    for userID, planetID in planetIDList:
        url = baseUrl.format(planetID)
        data, next = checkURLCache(url)
        if(not data):
            data = requests.get(url).json()
            cacheURLData(url, data, None)

        rows.append(data)

    rows = filterPlanetAttributeList(rows, True)
    return rows


"""
All methods for Movies
"""


def filterMovieAttributeList(data, isFavorite=False):
    filteredData = []
    for row in data:
        print(row)
        newRow = {}
        newRow["title"] = row.get("title")
        newRow["release_date"] = row.get("release_date")
        newRow["created"] = row.get("created")
        newRow["updated"] = row.get("edited")
        newRow["url"] = row.get("url")
        newRow["isFavorite"] = isFavorite
        filteredData.append(newRow)
    return filteredData


def getAllMovies():
    rows = []
    url = "https://swapi.dev/api/films/"
    while(url):
        data, next = checkURLCache(url)
        if(not data):
            result = requests.get(url).json()
            data = result["results"]
            next = result['next']
            data = filterMovieAttributeList(data)
            print(next)
            cacheURLData(url, data, next)

        rows.extend(data)
        url = next
    return rows


def getSpecificMovies(movieIDList):
    baseUrl = "http://swapi.dev/api/films/{}"
    rows = []

    for userID, movieID in movieIDList:
        url = baseUrl.format(movieID)
        data, next = checkURLCache(url)
        if(not data):
            data = requests.get(url).json()
            cacheURLData(url, data, None)

        rows.append(data)
    rows = filterMovieAttributeList(rows, True)
    return rows


"""
All methods for Characters
"""


def filterCharacterAttributeList(data, isFavorite=False):
    filteredData = []
    for row in data:
        print(row)
        newRow = {}
        newRow["name"] = row.get("name")
        newRow["created"] = row.get("created")
        newRow["updated"] = row.get("edited")
        newRow["url"] = row.get("url")
        newRow["birth_year"] = row.get("birth_year")
        newRow["isFavorite"] = isFavorite
        filteredData.append(newRow)
    return filteredData


def getAllCharacters():
    rows = []
    url = "https://swapi.dev/api/people/"
    while(url):
        data, next = checkURLCache(url)
        if(not data):
            result = requests.get(url).json()
            data = result["results"]
            data = filterCharacterAttributeList(data)
            next = result['next']
            print(next)
            cacheURLData(url, data, next)

        rows.extend(data)
        url = next
    return rows


def getSpecificCharacters(characterIDList):
    baseUrl = "https://swapi.dev/api/people/{}"
    rows = []

    for userID, characterID in characterIDList:
        url = baseUrl.format(characterID)
        data, next = checkURLCache(url)
        if(not data):
            data = requests.get(url).json()
            cacheURLData(url, data, None)
            print("character: ", data)

        rows.append(data)

    rows = filterCharacterAttributeList(rows, True)
    return rows
