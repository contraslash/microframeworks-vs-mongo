# import asyncio
import uvloop
from motor.motor_asyncio import AsyncIOMotorClient
from sanic import Sanic
from sanic.response import json, text
from bson.json_util import dumps

# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = Sanic(__name__)
mongo_connection = None
dummy_data = None


@app.listener('before_server_start')
async def configure_db(app, loop):
    print("before_server_start")
    global mongo_connection
    mongo_connection = AsyncIOMotorClient(
        "mongodb://localhost:27017/",
        io_loop=loop
    )
    global dummy_data
    dummy_data = mongo_connection.framework_benchmark.dummy_data


@app.route("/")
async def hello(request):
    return text('Hello World!')


@app.route("/data")
async def data(request):
    data = await dummy_data.find({}).to_list(10)
    return text(dumps(data))


app.run(host="0.0.0.0", port=8000, workers=3, debug=True)
