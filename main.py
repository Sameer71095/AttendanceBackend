#!/usr/bin/env python3
import asyncio
import os
import pickle
from http import HTTPStatus
from sanic import Sanic
from sanic import response
from sanic.exceptions import NotFound
from sanic_cors import CORS
from sanic.response import json
from handler.connectionPool import create_pool

from handler.routes import services
app = Sanic(__name__)

#app.config['DB_SETTINGS'] = TORTOISE_ORM

# Set the distance threshold using app.ctx.distance_threshold
app.ctx.distance_threshold = 0.4

# To set a variable on the Sanic instance, use `app.ctx._startup`
app.ctx._startup = True

# set a variable using ctx._startup
#app.ctx._startup['my_variable'] = 'my_value'
#CORS(app.ctx, automatic_options=True)


app.blueprint(services)


@app.middleware('request')
async def print_on_request(request):
    if request.method == 'OPTIONS':
        return response.json(None)



@app.listener('before_server_start')
async def init(app, loop):
    def load_pickle():
        _path = os.path.dirname(os.path.abspath(__file__)) + '/model/train_model.clf'
        with open(_path, 'rb') as f:
            return pickle.load(f)

    # distance threshold
    app.ctx.distance_threshold = 0.4
    # load classifier
    app.ctx.train_model = load_pickle()

    
@app.exception(NotFound)
async def ignore_404s(request, exception):
    return response.json({'status': HTTPStatus.NOT_FOUND, 'message': 'Route not found'})

    
if __name__ == "__main__":
    #asyncio.run(init_orm())
    #app.add_task(init_orm())
    app.run(host="0.0.0.0", port=8020, debug=True, workers=4, access_log=False)
