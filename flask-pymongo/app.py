from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask('framework_benchmark')
mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/data')
def data():
    return dumps(mongo.db.dummy_data.find({}))


if __name__ == '__main__':
    app.run()
