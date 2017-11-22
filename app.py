import bottle
from bottle import route, run, error, request, post, response, app, template
from beaker.middleware import SessionMiddleware
from sys import argv
#Bryngeir Ari & Páll Gunnar

@route('/')
def index():
    return template('<b>Palli er kominn á heroku</b>!', name=name)

run(host='0.0.0.0', port=argv[1], debug=True, reloader=True, app=app)  # keyrir server