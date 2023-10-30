import os
import pickle
from http import HTTPStatus
from sanic import Sanic
from sanic import response
from sanic.exceptions import NotFound
from sanic.log import logger
from sanic.response import json
from handler.routes import services
import dlib

def load_pickle():
    _path = os.path.dirname(os.path.abspath(__file__)) + '/model/train_model.clf'
    with open(_path, 'rb') as f:
        return pickle.load(f)

# Load model before server start
train_model = load_pickle()

app = Sanic(__name__)
app.ctx.distance_threshold = 0.39
app.ctx._startup = True
app.ctx.train_model = train_model
# Path to your 'shape_predictor_68_face_landmarks.dat' file
SHAPE_PREDICTOR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shape_predictor_68_face_landmarks.dat')

# Load the shape predictor model during startup
shape_predictor = dlib.shape_predictor(SHAPE_PREDICTOR_PATH)

# Then, in your Sanic application context, you can store the loaded shape_predictor
app.ctx.shape_predictor = shape_predictor
app.blueprint(services)

@app.middleware('request')
async def print_on_request(request):
    if request.method == 'OPTIONS':
        return response.json(None)

@app.exception(NotFound)
async def ignore_404s(request, exception):
    return response.json({'status': HTTPStatus.NOT_FOUND, 'message': 'Route not found'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8020, debug=True, workers=9, access_log=False)
