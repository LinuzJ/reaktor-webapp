from flask import Flask, render_template
from helpers import check_the_availability_data
import requests
import json

app = Flask(__name__)

def checkManufacturer(data_1, data_2, data_3):
    dataset = data_1 + data_2 + data_3
    export = []
    for product in dataset:
        if product['manufacturer'] not in export:
            export.append(product['manufacturer'])
    return export

def get_availability(list_with_manufacturers):
    return_variable = []
    holder_for_availability = []
    
    # get all data from all of the manufacturers 
    
    for manufacturer in list_with_manufacturers:
        print(manufacturer + " test inside loop")
        
        new_data = requests.get("https://bad-api-assignment.reaktor.com/v2/availability/" + manufacturer)
        response_data = new_data.json()
        list_with_dictionaries = response_data["response"]
        for item in list_with_dictionaries:
            print("im now inserting: ", item)
            holder_for_availability.append(item)
        


    # now we have a list of all the data with availability and id in a big array
    # now we want to sort and clean the data so olnly get availability linked to inside

    for product in holder_for_availability:
        try:
            return_variable.append({
                "id": product['id'],
                "availability": check_the_availability_data(product['DATAPAYLOAD'])
            })
        except:
            pass
    
    return return_variable



@app.route('/', methods=['GET'])
def api():
    req_gloves = requests.get("https://bad-api-assignment.reaktor.com/v2/products/gloves")
    req_facemasks = requests.get("https://bad-api-assignment.reaktor.com/v2/products/facemasks")
    req_beanies = requests.get("https://bad-api-assignment.reaktor.com/v2/products/beanies")
    
    json_data_gloves = json.loads(req_gloves.content)
    json_data_facemasks = json.loads(req_facemasks.content)
    json_data_beanies = json.loads(req_beanies.content)
    
    all_manufacturers = checkManufacturer(json_data_gloves, json_data_facemasks, json_data_beanies)

    get_availability(all_manufacturers)





    data_tot = {
        'gloves': json_data_gloves,
        'facemasks': json_data_facemasks,
        'beanies': json_data_beanies
         }

    return data_tot


if __name__ == "__main__":
    app.run(port=5000, debug=True)