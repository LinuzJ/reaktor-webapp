
from helpers import check_availability_data, check_manufacturer, add_availability, availability 
import requests
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



def get_data():
    
    retry_strategy = Retry(
    total=5,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["GET"],
    backoff_factor=1
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)


    try:
        req_gloves = http.get("https://bad-api-assignment.reaktor.com/v2/products/gloves")
        req_facemasks = http.get("https://bad-api-assignment.reaktor.com/v2/products/facemasks")
        req_beanies = http.get("https://bad-api-assignment.reaktor.com/v2/products/beanies")
    except Exception as err:
        print(err)
        return {}
    
    #   parse json
    json_data_gloves = json.loads(req_gloves.content)
    json_data_facemasks = json.loads(req_facemasks.content)
    json_data_beanies = json.loads(req_beanies.content)

    # make a list of all the manufacturers
    all_manufacturers = check_manufacturer((json_data_gloves + json_data_facemasks + json_data_beanies))

    # retrieve the availability of all products from the availability API
    try:
        availability_data = availability(all_manufacturers)
    except Exception as err:
        print(err)
        return {}

    data_tot = {
        'gloves': json_data_gloves,
        'facemasks': json_data_facemasks,
        'beanies': json_data_beanies
         }

    # get the data that has availability information
    new_data = add_availability(data_tot, availability_data)
    

    return new_data