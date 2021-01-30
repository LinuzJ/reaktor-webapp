from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from helpers import test_data
from flask_caching import Cache

cache = Cache()
app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'


cache.init_app(app)
cache_2 = {
    'gloves':[],
}


@app.route('/<category>', methods=['GET'])
def api(category):   
    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)
    data_from_cache = test_data
    resp = make_response({
        'data': data_from_cache[category][int(offset):int(offset+limit)],
        'totalItems': len(data_from_cache[category])
    })
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

# @cache.cached(timeout=300.0, key_prefix="data")
# def data():
#     return_data = get_data()
#     return return_data




if __name__ == "__main__":
    app.run(port=5000, debug=True)