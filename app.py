import bottle
from bottle import route, run, error, request, post, response, app, template
from beaker.middleware import SessionMiddleware
from sys import argv
#Bryngeir Ari & Páll Gunnar

@route('/')
def index():
    return template('<b>Palli er kominn á heroku</b>!')

run(host='0.0.0.0', port=argv[1])  # keyrir server