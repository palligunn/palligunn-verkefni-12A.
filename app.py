import bottle
from bottle import route, run, error, request, post, response, app, template
from beaker.middleware import SessionMiddleware
from sys import argv
#Bryngeir Ari & Páll Gunnar

@route('/<name>')
def index(name):
    return '<center><h1>'+name+'er kominn á heroku</h1></center>'

run(host='0.0.0.0', port=argv[1])  # keyrir server