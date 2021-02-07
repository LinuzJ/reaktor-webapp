from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from concurrent.futures import ThreadPoolExecutor
import time

app = Flask(__name__)

class Cached_data:
    def __init__(self, data: dict):
        self.cached = data
        self.previous = {}

cache_data = Cached_data({})

@app.route('/<category>', methods=['GET'])
def api(category):

    # getting the variables from the get request
    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)

    try:
            resp = make_response({
                'data': cache_data.cached[category][int(offset):int(offset)+int(limit)],
                'totalItems': len(cache_data.cached[category]),
                'columns': cache_data.cached[category][0]
            })
    except:
        # excecuted only at first load or if the data fetching fails
        if bool(cache_data.previous):
            resp = make_response({
                'data': cache_data.previous[category][int(offset):int(offset)+int(limit)],
                'totalItems': len(cache_data.previous[category]),
                'columns': cache_data.previous[category][0]
            })
        else:
            resp = make_response({
                'data': [],
                'totalItems': 0,
                'columns': []
            })

    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp

def update_data():
    while True:
        cache_data.previous = cache_data.cached
        cache_data.cached = get_data()
        time.sleep(300)


if __name__ == "__main__":

    executor = ThreadPoolExecutor(1)
    executor.submit(update_data)

    app.run(port=5000)

