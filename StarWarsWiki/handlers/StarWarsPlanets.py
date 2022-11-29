from tornado.web import RequestHandler
from helpers.functionalityHelper import (
    getPlanets,
    setFavoritePlanet,
    removeFavoritePlanet,
    # setFavoriteShip,
    # removeFavoriteShip
)


class PlanetData(RequestHandler):

    def get(self):
        user = self.get_argument('user', None)
        rows = getPlanets(user)
        result = {"rows": rows}
        self.write(result)

    def patch(self):
        user = self.get_argument('user')
        planetID = self.get_argument('planetID')
        setFavoritePlanet(user, planetID)

    def delete(self):
        user = self.get_argument('user')
        planetID = self.get_argument('planetID')
        removeFavoritePlanet(user, planetID)
