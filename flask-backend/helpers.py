import collections
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def availability(list_with_manufacturers):
    return_variable = []
    holder_for_availability = []

    retry_strategy = Retry(
        total=3,
        status_forcelist=[429, 500, 502, 503, 504],
        method_whitelist=["GET"],
        backoff_factor=2
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)


    # get all data from all of the manufacturers 
    for manufacturer in list_with_manufacturers:
        new_data = http.get("https://bad-api-assignment.reaktor.com/v2/availability/" + manufacturer)

        response = new_data.json()["response"]

        for item in response:
            holder_for_availability.append(item)
        

    # now we have a list of all the data with availability and id in a array
    # now we want to sort and clean the data so we only get availability linked to id

    for product in holder_for_availability:
        try:
            return_variable.append({
                "id": product['id'],
                "availability": check_availability_data(product['DATAPAYLOAD'])
            })
        except:
            pass
    
    return return_variable
    
def check_availability_data(string_with_info):
    return_list = string_with_info.split("<")
    return_list = [n.split(">") for n in return_list]
    return return_list[4][1]

def check_manufacturer(dataset):
    export = set()
    for product in dataset:
        export.add(product['manufacturer'])
    return list(export)

def add_availability(item_data, availability_data):
    return_data = []    
    av_dict = {item['id'].lower(): item for item in availability_data}


    for category in item_data:
    
        # we iterate through each category
        for item in item_data[category]:

            # then we check for matching item_data in the availability data
            if  item["id"].lower() in av_dict:
                 # add the availability data to the return dataset
                return_data.append({
                    "id":           item['id'],
                    "type":         item["type"],
                    "name":         item['name'],
                    "color":        item['color'],
                    "price":        item['price'],
                    "manufacturer": item['manufacturer'],
                    "availability": av_dict[item['id']]['availability']
                })

        # filtering the data into a dict with three different keys defined by the categories
    result = {
        'gloves': list(filter(lambda d: d['type'] == 'gloves', return_data)),
        'facemasks': list(filter(lambda d: d['type'] == 'facemasks', return_data)),
        'beanies': list(filter(lambda d: d['type'] == 'beanies', return_data))
    }
    return result 
    