import json
import re

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def get_json_from_response(response):
    #replace ' with "
    response = response.replace("'", '"')
    start = response.find('{')
    end = response.rfind('}')
    # Extract and print the content
    if start != -1 and end != -1:
        extracted = response[start:end+1]
        try:
            json_obj = json.loads(extracted)
            return json_obj
        except:
            pass

    match = re.search(r'\{[\s\S]*\}', response)
    if not match:
        return None
    match = match.group()
    return match


def get_list_from_response(response):
    response = response.replace("'", '"')
    start = response.find('[')
    end = response.rfind(']')
    # Extract and print the content
    if start != -1 and end != -1:
        extracted = response[start:end+1]
        try:
            json_obj = json.loads(extracted)
            return json_obj
        except:
            pass

    match = re.search(r'\[[\s\S]*\]', response)
    if not match:
        return None
    match = match.group()
    return match

def create_ontology_lists(data):
    superclasses = []
    subclasses = []
    subsubclasses = []  
    categories = []
    products = []
    for superclass in data.get("superclass", []):
        print(f"Superclass: {superclass['name']}")
        superclasses.append(superclass['name'])
        for subclass in superclass.get("subclass", []):
            print(f"  Subclass: {subclass['name']}")
            subclasses.append(subclass['name'])
            for subsubclass in subclass.get("subsubclass", []):
                print(f"    Subsubclass: {subsubclass['name']}")
                subsubclasses.append(subsubclass['name'])
                for category in subsubclass.get("category", []):
                    print(f"      Category: {category['name']}")
                    categories.append(category['name'])
                    for product in category.get("product", []):
                        print(f"        Product: {product['name']}")
                        products.append(product['name'])

    ontology = {
        "superclasses": superclasses,
        "subclasses": subclasses,
        "subsubclasses": subsubclasses,
        "categories": categories
    }
    # return superclasses, subclasses, subsubclasses, categories
    return ontology

def get_ontology_dict(data):
    ontology = {}
    ontology['superclasses'] = []
    superclasses = []
    for superclass in data.get("superclass", []):
        ontology[superclass['name']] = {}
        superclasses.append(superclass['name'])
        subclasses = []
        for subclass in superclass.get("subclass", []):
            ontology[superclass['name']][subclass['name']] = {}
            subclasses.append(subclass['name'])
            subsubclasses = []
            for subsubclass in subclass.get("subsubclass", []):
                ontology[superclass['name']][subclass['name']][subsubclass['name']] = {}
                subsubclasses.append(subsubclass['name'])
                categories = []
                for category in subsubclass.get("category", []):
                    categories.append(category['name'])
                ontology[superclass['name']][subclass['name']][subsubclass['name']]['categories'] = categories
            ontology[superclass['name']][subclass['name']]['subsubclasses'] = subsubclasses
        ontology[superclass['name']]['subclasses'] = subclasses
    ontology['superclasses'] = superclasses

    return ontology



if __name__ == "__main__":
    # json_obj = read_json('ontology.json')
    # data = get_ontology_dict(json_obj)

    # # print(data['superclasses'])
    # print(data['clothing']['traditional wear']['subsubclasses'])

    # #save this data to a file
    # with open('ontology_dict.json', 'w') as file:
    #     json.dump(data, file, indent=4)


    string = "['apple', 'banana', 'orange']"
    json_string = string.replace("'", '"')  # Replace single quotes with double quotes
    result = json.loads(json_string)
    print(type(result))