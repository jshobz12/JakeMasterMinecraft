
import bottle as b
import os

from sys import argv

from bottle import default_app, request, route, response, get

DEBUG = os.environ.get("DEBUG")

b.debug(True)

@route('/')
def index():
    return b.template('./landingpage.html')


@get('/js/<filename:re:.*\.js>')
def javascript(filename):
    return b.static_file(filename, root='js')


@get('/font<filename:re:.*\.ttf>')
def stylesheets(filename):
    return b.static_file(filename, root='font')


@get('/css<filename:re:.*\.css>')
def stylesheets(filename):
    return b.static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def img(filename):
    return b.static_file(filename, root='images')


if DEBUG:
	b.run(host='localhost', port=7000)
else:
	b.run(host='0.0.0.0', port=argv[1])