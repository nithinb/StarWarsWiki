from tornado.web import RequestHandler
from helpers.functionalityHelper import (
    getCharacter,
    setFavoriteCharacter,
    removeFavoriteCharacter,
)


class CharacterData(RequestHandler):

    def get(self):
        user = self.get_argument('user', None)
        rows = getCharacter(user)
        result = {"rows": rows}
        self.write(result)

    def patch(self):
        user = self.get_argument('user')
        planetID = self.get_argument('characterID')
        setFavoriteCharacter(user, planetID)

    def delete(self):
        user = self.get_argument('user')
        planetID = self.get_argument('characterID')
        removeFavoriteCharacter(user, planetID)
