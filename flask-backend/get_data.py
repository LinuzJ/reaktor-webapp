
from helpers import check_the_availability_data, checkManufacturer, match_id, get_availability 
import requests
import json

def get_data(): 
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

    return new_data