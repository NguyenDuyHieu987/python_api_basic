from flask import *
import json
import pymongo
from waitress import serve
from gevent.pywsgi import WSGIServer


myclient = pymongo.MongoClient("mongodb+srv://admin:hieusen123@cluster0.h6ko2rq.mongodb.net/movie_web_dev?retryWrites=true&w=majority")

app = Flask(__name__)

@app.route('/', methods=[ 'GET'])
def home_page():
    data_set = {'name':'hiếu'}
    json_dump = json.dumps(data_set)
    
    return json_dump

if __name__ == '__main__':
    http_server = WSGIServer(('', 777), app)
    http_server.serve_forever()