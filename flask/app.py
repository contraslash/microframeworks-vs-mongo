from flask import Flask
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client.framework_benchmark


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/data')
def data():
    return dumps(db.dummy_data.find({}))


if __name__ == '__main__':
    app.run()
