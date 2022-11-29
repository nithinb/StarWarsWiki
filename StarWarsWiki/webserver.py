# Tornado Imports
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application


# Handlers for different endpoints
from handlers.StarWarsPlanets import PlanetData
from handlers.StarWarsMovies import MovieData
from handlers.StarWarsCharacters import CharacterData


define('port', default=504, help='port to listen on')


def setupServer():
    """Construct and serve the tornado application."""
    app = Application([
        ('/planet', PlanetData),
        ('/movie', MovieData),
        ('/character', CharacterData)
    ], debug=True)
    http_server = HTTPServer(app)
    http_server.listen(options.port)

    try:
        print('Listening on http://localhost:%i' % options.port)
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
        print('Exited out of tornado IOLoop')
        raise KeyboardInterrupt
