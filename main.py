from flask import *
import json
import pymongo
from waitress import serve
from gevent.pywsgi import WSGIServer
from bson import json_util, ObjectId


myclient = pymongo.MongoClient(
    "mongodb+srv://admin:hieusen123@cluster0.h6ko2rq.mongodb.net/movie_web_dev?retryWrites=true&w=majority"
)

mydb = myclient["movie_web_dev"]
movies = mydb["movies"]
tvs = mydb["movies"]

a = {"hieu": 1, "hieu": 1, "hieu": 1, "hieu": 1}

app = Flask(__name__)


@app.route("/movie", methods=["GET"])
def movies_route():
    json_dump = json.loads(json_util.dumps(movies.find({})))
    return json_dump


@app.route("/tv", methods=["GET"])
def tvs_route():
    json_dump = json.loads(json_util.dumps(tvs.find_one()))
    return json_dump


@app.route("/image/<name>", methods=["GET"])
def img_route(name):
    if request.args.get("api", default="", type=str) == "hieu987":
        src_img = "./images/" + name
        return send_file(
            src_img,
            mimetype="image/gif",
        )


@app.route("/query", methods=["GET"])
def query_route():
    args = request.args
    print(args.get("id", default="", type=str))
    json_dump = json_util.dumps({"id": args.get("id", default="", type=str)})
    return json_dump


@app.route("/param/<name>", methods=["GET"])
def param_route(name):
    print(name)
    return name


if __name__ == "__main__":
    # app.run(port=7777)
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
