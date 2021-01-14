from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def api():
    req_gloves = requests.get("https://bad-api-assignment.reaktor.com/v2/products/gloves")
    req_facemasks = requests.get("https://bad-api-assignment.reaktor.com/v2/products/facemasks")
    req_beanies = requests.get("https://bad-api-assignment.reaktor.com/v2/products/beanies")
    
    json_data_gloves = json.loads(req_gloves.content)
    json_data_facemasks = json.loads(req_facemasks.content)
    json_data_beanies = json.loads(req_beanies.content)
    
    data_tot = {
        'gloves': json_data_gloves,
        'facemasks': json_data_facemasks,
        'beanies': json_data_beanies
         }

    return data_tot


if __name__ == "__main__":
    app.run(port=5000, debug=True)