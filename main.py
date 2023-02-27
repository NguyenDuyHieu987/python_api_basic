from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=[ 'GET'])
def home_page():
    data_set = {'name':'hiếu'}
    json_dump = json.dumps(data_set)
    
    return json_dump

if __name__ == '__main__':
    app.run(port=7777)