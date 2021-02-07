
from helpers import check_the_availability_data, check_manufacturer, add_availability, availability 
import requests
import json


def get_data(): 
    try:
        req_gloves = requests.get("https://bad-api-assignment.reaktor.com/v2/products/gloves")
        req_facemasks = requests.get("https://bad-api-assignment.reaktor.com/v2/products/facemasks")
        req_beanies = requests.get("https://bad-api-assignment.reaktor.com/v2/products/beanies")
    except Exception as err:
        print(err)
        return {}
    
    # make the recieved data readable
    json_data_gloves = json.loads(req_gloves.content)
    json_data_facemasks = json.loads(req_facemasks.content)
    json_data_beanies = json.loads(req_beanies.content)

    # make a list of all the manufacturers
    all_manufacturers = check_manufacturer((json_data_gloves + json_data_facemasks + json_data_beanies))


    # retrieve the availability of all products from the availability API
    try:
        availability_ = availability(all_manufacturers)
    except Exception as err:
        print(err)
        return {}

    data_tot = {
        'gloves': json_data_gloves,
        'facemasks': json_data_facemasks,
        'beanies': json_data_beanies
         }

    # get the data that has availability information
    new_data = add_availability(data_tot, availability_)
    

    return new_data