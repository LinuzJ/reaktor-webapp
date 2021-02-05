from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from concurrent.futures import ThreadPoolExecutor
import time

app = Flask(__name__)

cache_data = []

@app.route('/<category>', methods=['GET'])
def api(category):
    
    global cache_data

    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)
    print(int(offset), int(int(offset)+int(limit)))
    try:
        resp = make_response({
            'data': cache_data[category][int(offset):int(int(offset)+int(limit))],
            'totalItems': len(cache_data[category]),
            'columns': cache_data[category][0]
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
    global cache_data

    while True:
        cache_data = get_data()
        time.sleep(500)



if __name__ == "__main__":

    executor = ThreadPoolExecutor(1)
    executor.submit(update_data)

    app.run(port=5000)

