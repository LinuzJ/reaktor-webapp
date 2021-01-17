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

    for category in item_data:
        
        # we iterate through each category
        for item in item_data[category]:
            
            # here we iterate through each item in this category
            # then we check for matching item_data
            for row in availability_data:
                
                # here we iterate through each row in the availability dataset
                if  row["id"].lower() == item["id"].lower():

                    # add the availability data to the return dataset
                    return_data.append({
                        "id":           item['id'],
                        "type":         item["type"],
                        "name":         item['name'],
                        "color":        item['color'],
                        "price":        item['price'],
                        "manufacturer": item['manufacturer'],
                        "availability": row['availability']
                    })         
    return return_data