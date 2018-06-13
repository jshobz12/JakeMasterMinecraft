
from bottle import route, get
import bottle as b
from sys import argv


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


def main():
	b.run(host='0.0.0.0', port=argv[1])

if __name__ == "__main__":
    main()