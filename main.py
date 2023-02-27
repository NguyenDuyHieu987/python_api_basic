from flask import *
import json
import pymongo
from waitress import serve
from gevent.pywsgi import WSGIServer
from bson import json_util, ObjectId


myclient = pymongo.MongoClient("mongodb+srv://admin:hieusen123@cluster0.h6ko2rq.mongodb.net/movie_web_dev?retryWrites=true&w=majority")

mydb = myclient["movie_web_dev"]
movies = mydb["movies"]
tvs = mydb["movies"]



app = Flask(__name__)

@app.route('/movie', methods=[ 'GET'])
def movies_route():
    json_dump = json.loads(json_util.dumps(movies.find_one()))
    return json_dump

@app.route('/tv', methods=[ 'GET'])
def tvs_route():
    json_dump = json.loads(json_util.dumps(tvs.find_one()))
    return json_dump

if __name__ == '__main__':
    # app.run(port=7777)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()