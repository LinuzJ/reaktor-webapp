import collections

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
        'facemasks': list(filter(lambda d: d['type'] == 'fasemasks', return_data)),
        'beanies': list(filter(lambda d: d['type'] == 'beanies', return_data))
    }
    
    return result