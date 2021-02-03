from flask import Flask, render_template, request, Response, jsonify, make_response
from get_data import get_data
from helpers import test_data
import asyncio



app = Flask(__name__)

cache_data = []

async def update_data():
    print("inside update pre loop")
    global cache_data
    print("inside update and starting to update data")
    await asyncio.sleep(5)
    cache_data = test_data
    # cache_data = await get_data()
    print("the data has been updated!")
    # await asyncio.sleep(70)



@app.route('/<category>', methods=['GET'])
def api(category):
    
    global cache_data

    offset  = request.args.get('o', None)
    limit  = request.args.get('l', None)
    data_from_cache = test_data
    
    try:
        resp = make_response({
            'data': cache_data[category][int(offset):int(offset+limit)],
            'totalItems': len(cache_data[category]),
            'columns': cache_data[category][0]
        })
    except:
        resp = make_response({
            'data': [],
            'totalItems': 0,
            'columns': []
        })
    
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp



if __name__ == "__main__":
    app.run(port=5000, debug=True)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_data())