from tornado.web import RequestHandler
from helpers.functionalityHelper import (
    getMovies,
    setFavoriteMovie,
    removeFavoriteMovie,
)


class MovieData(RequestHandler):

    def get(self):
        user = self.get_argument('user', None)
        rows = getMovies(user)
        result = {"rows": rows}
        self.write(result)

    def patch(self):
        user = self.get_argument('user')
        planetID = self.get_argument('planetID')
        setFavoriteMovie(user, planetID)

    def delete(self):
        user = self.get_argument('user')
        planetID = self.get_argument('planetID')
        removeFavoriteMovie(user, planetID)
