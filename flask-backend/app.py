from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from helpers import test_data
import asyncio



app = Flask(__name__)

cache_data = get_data()

async def update_data():
    print("inside update")
    while True:
        global cache_data
        print("inside update and starting to update data")
        cache_data = await get_data()
        print("UPDATED THE DA TA!")
        await asyncio.sleep(70)



@app.route('/<category>', methods=['GET'])
def api(category):
    global cache_data
    update_data()   
    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)
    data_from_cache = test_data
    resp = make_response({
        'data': cache_data[category][int(offset):int(offset+limit)],
        'totalItems': len(cache_data[category]),
        'columns': cache_data[category][0]
    })
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == "__main__":
    app.run(port=5000, debug=True)
    loop = asyncio.get_event_loop()
    loop.run_forever