from flask import Flask, render_template
from get_data import get_data
from flask_caching import Cache
from random import randint

cache = Cache()
app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'

cache.init_app(app)

@app.route('/', methods=['GET'])
def api():
    dataa = data()
    return dataa

@cache.cached(timeout=300.0, key_prefix="data")
def data():
    return_data = get_data()
    return return_data

if __name__ == "__main__":
    app.run(port=5000, debug=True)