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



test_data = {
  "beanies": [
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "d487dbb1b404728a8e0fa3b9", 
      "manufacturer": "hennex", 
      "name": "YYJEDAL WIND SHINE", 
      "price": 22, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "2d262ee988846043051", 
      "manufacturer": "abiplos", 
      "name": "HEMUP RAIN", 
      "price": 40, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black", 
        "purple"
      ], 
      "id": "c1a2d6cd622ad3997fa2142", 
      "manufacturer": "ippal", 
      "name": "SOPFOL SHINE", 
      "price": 40, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "7c87f8dbee644a873f4439", 
      "manufacturer": "abiplos", 
      "name": "EMILMO FLOWER", 
      "price": 90, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "008f8123b4b03a10b8b", 
      "manufacturer": "ippal", 
      "name": "MO\u00d6ISGIN CITY SHINE", 
      "price": 34, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white", 
        "yellow"
      ], 
      "id": "b1c856f2d71659920ce3da", 
      "manufacturer": "laion", 
      "name": "YYTAIJE WIND", 
      "price": 33, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green", 
        "white"
      ], 
      "id": "568180886299b13f47057dd5", 
      "manufacturer": "laion", 
      "name": "MOVE SHINE WIND", 
      "price": 79, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red", 
        "grey"
      ], 
      "id": "3414819c839ff967b5cfa7", 
      "manufacturer": "hennex", 
      "name": "ILOOTFOL MAGIC RAPTOR", 
      "price": 94, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "45258d6fa5a35c4d69881216", 
      "manufacturer": "laion", 
      "name": "OOTEMREV BUCK", 
      "price": 80, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "c2df8e7644c45e7164", 
      "manufacturer": "laion", 
      "name": "REVFOL\u00c4N FLOWER", 
      "price": 68, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "yellow"
      ], 
      "id": "8198772dd15de9c069", 
      "manufacturer": "abiplos", 
      "name": "\u00c4NTAINY BRIGHT", 
      "price": 27, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "e0d8ec075a84161a576a", 
      "manufacturer": "hennex", 
      "name": "LEAMO ALPINE", 
      "price": 50, 
      "type": "beanies"
    }, 
    {
      "availability": "LESSTHAN10", 
      "color": [
        "purple"
      ], 
      "id": "b032ee7b4743357e546", 
      "manufacturer": "ippal", 
      "name": "\u00d6IS\u00c4NAK BOON RAPTOR", 
      "price": 60, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "fae438ecdbeb47af0f651b2e", 
      "manufacturer": "abiplos", 
      "name": "FOLREVOOT METROPOLIS RAIN", 
      "price": 457, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple", 
        "red"
      ], 
      "id": "3fb91a9889de1e9bc9728db7", 
      "manufacturer": "laion", 
      "name": "DALREVNY RAIN BRIGHT", 
      "price": 56, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "d4625240f776cba1bce", 
      "manufacturer": "hennex", 
      "name": "VELEAFOL FANTASY", 
      "price": 20, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "6a8f4b83542455c4d6", 
      "manufacturer": "ippal", 
      "name": "JEDALEM HYDRA", 
      "price": 65, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green"
      ], 
      "id": "62b833b887bba544ea", 
      "manufacturer": "abiplos", 
      "name": "ILMO ROOM", 
      "price": 31, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white", 
        "red"
      ], 
      "id": "c3ffd33e432f47f4b5", 
      "manufacturer": "ippal", 
      "name": "\u00d6ISSOP LIGHT", 
      "price": 33, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "a17d24053671920a9cbf3686", 
      "manufacturer": "ippal", 
      "name": "MO\u00c4NIL ROOM GREEN", 
      "price": 68, 
      "type": "beanies"
    }, 
    {
      "availability": "LESSTHAN10", 
      "color": [
        "black", 
        "green"
      ], 
      "id": "3c72e9fb0b4a87ea7e6245", 
      "manufacturer": "ippal", 
      "name": "REVKOL TYRANNUS", 
      "price": 10, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "dd9d4510a3d105bedd93299", 
      "manufacturer": "abiplos", 
      "name": "FOLNY BANG", 
      "price": 24, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black", 
        "green"
      ], 
      "id": "e29ce24d8bb40865aa9", 
      "manufacturer": "hennex", 
      "name": "KOLVEIL WIND", 
      "price": 53, 
      "type": "beanies"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "93db6d2fbf74420f0330", 
      "manufacturer": "hennex", 
      "name": "REVSOPFOL TREE", 
      "price": 97, 
      "type": "beanies"
    }
    ], 
  "facemasks": [
    {
      "availability": "INSTOCK", 
      "color": [
        "blue", 
        "green"
      ], 
      "id": "30356b372adadb07590", 
      "manufacturer": "abiplos", 
      "name": "MOOOTEM ROOM RAIN", 
      "price": 63, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green"
      ], 
      "id": "edbc1d98b24597f6ee47f253", 
      "manufacturer": "hennex", 
      "name": "\u00c4NUPDAL RAPTOR SWEET", 
      "price": 396, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green", 
        "purple"
      ], 
      "id": "af16ae14b5d2513f16bf216", 
      "manufacturer": "abiplos", 
      "name": "AKMOVE METROPOLIS", 
      "price": 19, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "d719d266e3dfca5e9c0c54", 
      "manufacturer": "laion", 
      "name": "GINOOT\u00c4N STAR ROOM", 
      "price": 71, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "c17937bccbbc8f8756cd8", 
      "manufacturer": "abiplos", 
      "name": "KOLVE\u00c4N RAPTOR", 
      "price": 78, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "f0f6649ba5738674aaf", 
      "manufacturer": "hennex", 
      "name": "EMAKREV EARTH LIGHT", 
      "price": 37, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "e204f0a72699fb07d0", 
      "manufacturer": "ippal", 
      "name": "LEAHEM RAPTOR TYRANNUS", 
      "price": 23, 
      "type": "facemasks"
    },
    {
      "availability": "INSTOCK", 
      "color": [
        "white", 
        "blue"
      ], 
      "id": "daaff8276f34b11ba5227e", 
      "manufacturer": "umpante", 
      "name": "OOTIL TREE BANG", 
      "price": 49, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "1d8ffc654fd40e6365e2e0a", 
      "manufacturer": "ippal", 
      "name": "NYAKYY METROPOLIS", 
      "price": 54, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "8f2265dcb317f5b13a85a", 
      "manufacturer": "umpante", 
      "name": "AKKOL GREEN EARTH", 
      "price": 76, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "62de269a6db1993d98e91b", 
      "manufacturer": "hennex", 
      "name": "AK\u00c4N ANIMAL FANTASY", 
      "price": 10, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "916f40da7f13978a30d", 
      "manufacturer": "ippal", 
      "name": "REVHEMAK LIGHT WIND", 
      "price": 98, 
      "type": "facemasks"
    }, 
    {
      "availability": "LESSTHAN10", 
      "color": [
        "red"
      ], 
      "id": "0b1b1479ced2e9d9a52c41", 
      "manufacturer": "abiplos", 
      "name": "EMDAL TYRANNUS", 
      "price": 27, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "281d657c6417e37e452c", 
      "manufacturer": "abiplos", 
      "name": "VEEM BANG ROOM", 
      "price": 706, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "3dcc9bd66354ea063009b", 
      "manufacturer": "niksleh", 
      "name": "HEMEMKOL JUMP", 
      "price": 35, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "blue"
      ], 
      "id": "4d3a2d0efe4e9064c731", 
      "manufacturer": "niksleh", 
      "name": "\u00c4NVE EARTH BOON", 
      "price": 62, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "blue"
      ], 
      "id": "8a8b9ffe458e0aaeb16", 
      "manufacturer": "laion", 
      "name": "LEAOOTSOP RAIN", 
      "price": 26, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green"
      ], 
      "id": "48e8299553bcef3cea1b", 
      "manufacturer": "umpante", 
      "name": "HEM\u00d6ISAK TYRANNUS", 
      "price": 83, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "485075cdf44ce7914f5f04", 
      "manufacturer": "ippal", 
      "name": "\u00c4NILJE BRIGHT TYRANNUS", 
      "price": 56, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "blue"
      ], 
      "id": "5cb88bc3fcac3bb6c5e78e", 
      "manufacturer": "umpante", 
      "name": "REVIL FANTASY BUCK", 
      "price": 92, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "5c9bf9742619282cbc6b", 
      "manufacturer": "hennex", 
      "name": "AKNYFOL ALPINE STAR", 
      "price": 32, 
      "type": "facemasks"
    }, 
    {
      "availability": "LESSTHAN10", 
      "color": [
        "grey", 
        "black"
      ], 
      "id": "17b81b65281ca75cff75", 
      "manufacturer": "hennex", 
      "name": "SOPGINDAL BANG", 
      "price": 21, 
      "type": "facemasks"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "fa23ce808acf6f20d45235f9", 
      "manufacturer": "abiplos", 
      "name": "\u00d6ISEM BRIGHT SHINE", 
      "price": 335, 
      "type": "facemasks"
    }],
  "gloves": [
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "2d6689eb99b693d59506", 
      "manufacturer": "laion", 
      "name": "GINILYY EARTH", 
      "price": 18, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green"
      ], 
      "id": "9f10f153e20f8c73ec5922b6", 
      "manufacturer": "laion", 
      "name": "GINTAIUP LIGHT", 
      "price": 91, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "82c66ecc1fa56616af029", 
      "manufacturer": "laion", 
      "name": "MOSOPKOL SHINE", 
      "price": 84, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "cc81fe5a93b6fa82ef1b0", 
      "manufacturer": "umpante", 
      "name": "YYJESOP BOON", 
      "price": 82, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "01e44f4d08e6aa0b8c0", 
      "manufacturer": "niksleh", 
      "name": "HEMMOSOP ALPINE", 
      "price": 56, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "bdaccb20549043ccc488d54", 
      "manufacturer": "hennex", 
      "name": "ILEM BRIGHT", 
      "price": 284, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "a051cc8bbc4735fe190d37", 
      "manufacturer": "niksleh", 
      "name": "SOPHEMAK HYDRA SWEET", 
      "price": 28, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "yellow"
      ], 
      "id": "32121e17e942b49fe9548", 
      "manufacturer": "niksleh", 
      "name": "TAIFOL HYDRA", 
      "price": 21, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "5a001478f4d0b2e35f0e210b", 
      "manufacturer": "niksleh", 
      "name": "YYNYTAI BANG BRIGHT", 
      "price": 909, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "5efa92c7dc9754cf75fb136", 
      "manufacturer": "umpante", 
      "name": "VELEADAL SLIP", 
      "price": 13, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "112e158b962f79c3f97", 
      "manufacturer": "niksleh", 
      "name": "\u00d6ISFOLIL LIGHT", 
      "price": 43, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "0d59ba713b87edb8acd55c36", 
      "manufacturer": "laion", 
      "name": "REVHEMSOP TYRANNUS", 
      "price": 96, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "d8dcbb6b612d4fe1cf1935", 
      "manufacturer": "abiplos", 
      "name": "REVDALHEM BOON LIGHT", 
      "price": 96, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "8620a67843a4d3b0a8b9c3", 
      "manufacturer": "laion", 
      "name": "SOP\u00c4NDAL ANIMAL", 
      "price": 881, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple", 
        "black"
      ], 
      "id": "0db8413e55741dcb4e382", 
      "manufacturer": "hennex", 
      "name": "UPYYHEM STAR", 
      "price": 32, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "3a46f27b5a5b42cc25", 
      "manufacturer": "ippal", 
      "name": "HEMUPEM RAIN BUCK", 
      "price": 63, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "blue"
      ], 
      "id": "663371b09ef38f111853cb2e", 
      "manufacturer": "laion", 
      "name": "\u00d6IS\u00c4N BUCK", 
      "price": 24, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "24187cb90aa56ab7601", 
      "manufacturer": "abiplos", 
      "name": "ILNYVE TREE", 
      "price": 55, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey", 
        "green"
      ], 
      "id": "d6448716573af75c09877", 
      "manufacturer": "niksleh", 
      "name": "JEOOT FANTASY", 
      "price": 11, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "fa12cbf0ac774d162a9286bc", 
      "manufacturer": "abiplos", 
      "name": "FOLTAIUP NORMAL", 
      "price": 76, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "7956095210a1bfd4c84539e", 
      "manufacturer": "umpante", 
      "name": "OOTVEIL MAGIC FANTASY", 
      "price": 78, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "6a9d23e995fef727803", 
      "manufacturer": "hennex", 
      "name": "HEMDALIL NORMAL", 
      "price": 67, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "green", 
        "white"
      ], 
      "id": "48bc6883cf4994f126", 
      "manufacturer": "niksleh", 
      "name": "UPYY ALPINE EARTH", 
      "price": 74, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "yellow"
      ], 
      "id": "8adeff02ef0fd51f685ed8", 
      "manufacturer": "hennex", 
      "name": "GINMOSOP RAIN MULTI", 
      "price": 42, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black", 
        "red"
      ], 
      "id": "d9f5c8f97543ef413d8288e2", 
      "manufacturer": "niksleh", 
      "name": "DALMOSOP BANG SWEET", 
      "price": 30, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "a86d8d5cfe026bedb82ba", 
      "manufacturer": "laion", 
      "name": "UPNYMO METROPOLIS", 
      "price": 80, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "7bd744158225046c25", 
      "manufacturer": "laion", 
      "name": "KOLSOP\u00d6IS CITY", 
      "price": 50, 
      "type": "gloves"
    }, 
    {
      "availability": "LESSTHAN10", 
      "color": [
        "grey"
      ], 
      "id": "c9f65c157e6ed065a95dfd9", 
      "manufacturer": "niksleh", 
      "name": "AKLEATAI BUCK TREE", 
      "price": 54, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "7d9215733b1fa95aa784b22", 
      "manufacturer": "ippal", 
      "name": "UPNY METROPOLIS", 
      "price": 51, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "blue"
      ], 
      "id": "86a0b0d0a5acde3729ef44", 
      "manufacturer": "hennex", 
      "name": "EMUPIL METROPOLIS", 
      "price": 42, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "white"
      ], 
      "id": "f1b9a4a4f547868816f8794", 
      "manufacturer": "ippal", 
      "name": "SOPOOTHEM TREE", 
      "price": 80, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple"
      ], 
      "id": "d929a9a90c32b8100ecae02c", 
      "manufacturer": "umpante", 
      "name": "\u00c4NVEGIN SHINE", 
      "price": 28, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey"
      ], 
      "id": "8d98d19e49f73b2351b042", 
      "manufacturer": "niksleh", 
      "name": "NYUPJE BUCK STAR", 
      "price": 84, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "grey", 
        "yellow"
      ], 
      "id": "d0cb59aa753e58a316b", 
      "manufacturer": "hennex", 
      "name": "LEAUP SLIP", 
      "price": 40, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "purple", 
        "red"
      ], 
      "id": "b502ee13d8ff5547d83e", 
      "manufacturer": "umpante", 
      "name": "TAINYREV SWEET", 
      "price": 92, 
      "type": "gloves"
    }, 
    {
      "availability": "OUTOFSTOCK", 
      "color": [
        "white"
      ], 
      "id": "42cddb4b0f62210435c2", 
      "manufacturer": "laion", 
      "name": "GINAKMO RAIN ROOM", 
      "price": 996, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "red"
      ], 
      "id": "d99657f3af56112e8fd653b", 
      "manufacturer": "abiplos", 
      "name": "EMKOLOOT FLOWER", 
      "price": 28, 
      "type": "gloves"
    }, 
    {
      "availability": "INSTOCK", 
      "color": [
        "black"
      ], 
      "id": "4bde0c3c8c63c401bb", 
      "manufacturer": "abiplos", 
      "name": "YYJEAK BOON", 
      "price": 71, 
      "type": "gloves"
    }, 
    {
      "availability": "OUTOFSTOCK", 
      "color": [
        "red"
      ], 
      "id": "37da1b9ea1324c3d6ab3b6", 
      "manufacturer": "laion", 
      "name": "DALNY EARTH", 
      "price": 85, 
      "type": "gloves"
    }
  ]
}