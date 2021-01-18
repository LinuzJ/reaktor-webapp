from flask import Flask, render_template
from helpers import check_the_availability_data, checkManufacturer, match_id
import requests
import json

app = Flask(__name__)
cache = None



def get_availability(list_with_manufacturers):
    return_variable = []
    holder_for_availability = []
    
    # get all data from all of the manufacturers 
    
    for manufacturer in list_with_manufacturers:

        
        new_data = requests.get("https://bad-api-assignment.reaktor.com/v2/availability/" + manufacturer)
        print(manufacturer + " test inside loop")
        response_data = new_data.json()
        list_with_dictionaries = response_data["response"]
        for item in list_with_dictionaries:
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
    global cache
    if cache is not None:
        return cache

    req_gloves = requests.get("https://bad-api-assignment.reaktor.com/v2/products/gloves")
    req_facemasks = requests.get("https://bad-api-assignment.reaktor.com/v2/products/facemasks")
    req_beanies = requests.get("https://bad-api-assignment.reaktor.com/v2/products/beanies")
    
    # make the recieved data readable
    json_data_gloves = json.loads(req_gloves.content)
    json_data_facemasks = json.loads(req_facemasks.content)
    json_data_beanies = json.loads(req_beanies.content)
    

    # make a list of all the manufacturers
    all_manufacturers = checkManufacturer(json_data_gloves, json_data_facemasks, json_data_beanies)

    # retrieve the availability of all products from the other API
    availability = get_availability(all_manufacturers)

    data_tot = {
        'gloves': json_data_gloves,
        'facemasks': json_data_facemasks,
        'beanies': json_data_beanies
         }

    # get the data that has availability information
    new_data = match_id(data_tot, availability)

    # new_data = match_id(data_tot, availability)
    cache = new_data
    return new_data


if __name__ == "__main__":
    app.run(port=5000, debug=True)