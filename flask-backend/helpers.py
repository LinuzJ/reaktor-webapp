import collections
import requests

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
    
def check_the_availability_data(string_with_info):
    return_list = string_with_info.split("<")
    return_list = [n.split(">") for n in return_list]
    return return_list[4][1]

def checkManufacturer(data_1, data_2, data_3):
    dataset = data_1 + data_2 + data_3
    export = []
    for product in dataset:
        if product['manufacturer'] not in export:
            export.append(product['manufacturer'])
    return export

def match_id(item_data, availability_data):
    return_data = []
    av_dict = {item['id'].lower(): item for item in availability_data}

    for category in item_data:
        
        # we iterate through each category
        for item in item_data[category]:
            
            # then we check for matching item_data in the availability data
            if  item["id"].lower() in av_dict:

                # add the availability data to the return dataset
                return_data.append({
                    "Id":           item['id'],
                    "Type":         item["type"],
                    "Name":         item['name'],
                    "Color":        item['color'],
                    "Price":        item['price'],
                    "Manufacturer": item['manufacturer'],
                    "Availability": av_dict[item['id']]['availability']
                })

    # filtering the data into a dict with three different keys defined by the categories
    result = {
        'gloves': list(filter(lambda d: d['Type'] == 'gloves', return_data)),
        'facemasks': list(filter(lambda d: d['Type'] == 'facemasks', return_data)),
        'beanies': list(filter(lambda d: d['Type'] == 'beanies', return_data))
    }
    
    return result