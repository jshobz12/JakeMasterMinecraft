from bottle import route, run, get
import bottle as b


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
    run(host="localhost", port=7001)


if __name__== '__main__':
    main()