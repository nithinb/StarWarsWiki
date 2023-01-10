# Star Wars Wiki

This code allows you to setup the backend for a Star Wars Wiki page with user based customizations like favorites in movies, characters, planets.

The supported Rest API Calls are as follows:

``` json
Endpoint: /planet
Supported methods: GET, PATCH, DELETE

Endpoint: /movie
Supported methods: GET, PATCH, DELETE

Endpoint: /character
Supported methods: GET, PATCH, DELETE
```

## Instructions to execute the code

* Kindly install `Python 3.10.6`

* Install the libraries required for Python using pip
  * pip install -r requirements.txt

* Start the service by running the following command. It is worth noting that the server stars up on the port `504`

``` shell

python StarWarsWiki.py
```

* The first run of this application might be a tad bit slower (Couple of seconds utmost) since the required tables and indexes need to be created but the next run should be quite quick.

---

## Interacting with /planet endpoint

### GET Request

With the `GET` request you can provide an option argument of `user` which represents the unique userID, which would return the list of planets that were marked as favorite for a particular user. If no argument is provided we return the entire list of Planets that are a part of the Star Wars Universe.

### PATCH Request

With the `PATCH` request you **have** to provide the `user` and `planetID` arguments, which allow you to set that particular planetID as a favorite for that particular user

### DELETE Request

With the `DELETE` request you **have** to provide the `user` and `planetID` arguments, which allow you to delete that particular planetID as a favorite for that particular user

---

## Interacting with /movie endpoint

### GET Request

With the `GET` request you can provide an option argument of `user` which represents the unique userID, which would return the list of movies that were marked as favorite for a particular user. If no argument is provided we return the list of movies that are a part of the Star Wars Franchise.

### PATCH Request

With the `PATCH` request you **have** to provide the `user` and `movieID` arguments, which allow you to set that particular movieID as a favorite for that particular user

### DELETE Request

With the `DELETE` request you **have** to provide the `user` and `movieID` arguments, which allow you to delete that particular movieID as a favorite for that particular user

---

## Interacting with /character endpoint

### GET Request

With the `GET` request you can provide an option argument of `user` which represents the unique userID, which would return the list of characters that were marked as favorite for a particular user. If no argument is provided we return the entire list of Characters that are a part of the Star Wars Universe.

### PATCH Request

With the `PATCH` request you **have** to provide the `user` and `characterID` arguments, which allow you to set that particular characterID as a favorite for that particular user

### DELETE Request

With the `DELETE` request you **have** to provide the `user` and `characterID` arguments, which allow you to delete that particular characterID as a favorite for that particular user

---

## Unique Features

* Since we are using sqllite database which is a file based db, the setup is very easy across systems and makes it really convinient to run across systems

* We maintain a table in our database called URLCache which stores the data that we receive from our API calls to SWAPI so that we can speed up the process of data access and also avoid hitting the Rate limit in the long run.
  * Since there is a possibility for data to be updated we also maintain an expiry for the cached data such that if the data is older than one hour we directly fetch from the API instead of using stale data.

* We also have a DB cleaner process that essentially wakes up once every hour and cleans up our cache table to avoid bloating and also save storage

* Since are caching is done at a DB level if you are running more than one instance of this service, this cache will be maintained across instances which will make it quite efficient in terms of network calls

---

## Features

Due to few unforseen circumstances I had very little time to finish this assignment so there are a few features that were part of the requirement that are not supported:

### Features Supported

* MUST load planets and movies from the JSON API provided by `https://swapi.dev/`

* MUST expose list APIs - one for movies and one for planets

* MUST expose APIs to add a movie and planet as a favourite

* The favourites must be stored per user (user_id can simply be passed in the request, there is no need for authentication)

* The planet list API must return the name, created, updated, url and is_favourite fields

* The movies list API must return the title, release_date, created, updated, url and is_favourite fields

### Features Unsupported

* The favourite API should also allow setting a custom title/name to the movie/planet

* If the custom name is set by the user then that should be returned as the name/title and it should be used when searching

* Additionally the list APIs must support searching by title/name

---

#### Keywords

* characterID: This is the ID for a particular character that is used as part of the SWAPI.
  * For example: characterID of 1 refers to Luke Skywalker, as can be accessed via the API call to the URL: `https://swapi.dev/api/people/1/`

* planetID: This is the ID for the particular planet that is used as part of the SWAPI.
  * For example: planetID of 1 refers to Tatooine, as can be accessed via the API call to the URL: `https://swapi.dev/api/planets/1`

* movieID: This is the ID of the particular movie that is used as part of the SWAPI.
  * For example: movieID of 1 refers to "Star Wards Chapter 4: A New Hope", as can be accessed via the API call to the URL: `https://swapi.dev/api/films/1`
  
  

ghs_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
