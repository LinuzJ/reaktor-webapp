from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from helpers import test_data



app = Flask(__name__)



@app.route('/<category>', methods=['GET'])
def api(category):   
    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)
    data_from_cache = test_data
    resp = make_response({
        'data': data_from_cache[category][int(offset):int(offset+limit)],
        'totalItems': len(data_from_cache[category]),
        'columns': data_from_cache[category][0]
    })
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == "__main__":
    app.run(port=5000, debug=True)