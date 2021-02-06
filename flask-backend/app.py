from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from concurrent.futures import ThreadPoolExecutor
import time

app = Flask(__name__)

class Cached_data:
    def __init__(self, data: dict):
        self.cahced = data

cache_data = Cached_data({})

@app.route('/<category>', methods=['GET'])
def api(category):

    # getting the variables from the get request
    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)

    try:
        resp = make_response({
            'data': cache_data.data[category][int(offset):int(offset)+int(limit)],
            'totalItems': len(cache_data.data[category]),
            'columns': cache_data.data[category][0]
        })
    except:
        # excecuted only at first load or if the data fetching fails
        resp = make_response({
            'data': [],
            'totalItems': 0,
            'columns': []
        })

    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp

def update_data():

    while True:
        new_data = get_data()
        if not data:
            pass
        else:
            cache_data.data = new_data 
        time.sleep(10)


if __name__ == "__main__":

    executor = ThreadPoolExecutor(1)
    executor.submit(update_data)

    app.run(port=5000)

