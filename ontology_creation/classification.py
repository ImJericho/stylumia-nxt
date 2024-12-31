import json
import re
from sentence_transformers import SentenceTransformer, util
from ollama import chat
from ollama import ChatResponse
import load_ontology as lo



def llm_response(msg, model='phi3'):
    if model == 'llama3.2':
        model = 'llama3.2'
    else:
        model = 'phi3'

    response: ChatResponse = chat(model=model, messages=[
        {
            'role': 'user',
            'content': msg,
        },
    ])
    return response.message.content



def get_class_from_text_using_llm(text, class_list):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    text_embedding = model.encode(text, convert_to_tensor=True)
    class_embeddings = model.encode(class_list, convert_to_tensor=True)
    similarities = util.cos_sim(text_embedding, class_embeddings)[0]
    
    # Create a dictionary of class: similarity
    similarity_dict = {cls: float(similarity) for cls, similarity in zip(class_list, similarities)}
    print(f"Similarity Dictionary: {similarity_dict}")
    
    return similarity_dict

def get_class_from_text_using_ollama(datapoint, class_list, debug=False):
    prompt = (
        "I have a fashion item described as follows: {msg}. "
        "Based on this description, identify the most suitable class for the item from this list {class_list}. "
        "If the item does not match any of the existing classes, feel free to assign a new class or indicate that it doesn't belong to any known category. "
        "Your response should be contain only a JSON object nothing else with the key 'class' and the value as the determined class name (either from the provided list, a new class, or 'None' if no match is found)."
    )
    prompt = prompt.format(msg=datapoint, class_list=class_list)
    

    for i in range(10):
        response = llm_response(prompt)
        # print(f"Attempt {i+1}, ({response})")
        try:
            # json_obj = json.loads(response)
            json_obj = lo.get_json_from_response(response)
            break
        except:
            if debug:
                print("Error in get_json_from_response")
            continue
    
    if json_obj['class'] not in class_list:
        if debug:
            print(f"Invalid class: {json_obj['class']}")
        return True, json_obj['class']
    
    if debug:
        print(f"Valid class: {json_obj['class']}")
    return False, json_obj['class']


def get_filtered_properties_from_attribute(attribute_dict, debug=False):

    prompt = (
        "I have a fashion item with the following attributes: {attribute_list}. "
        "Based on this attribute, filter out the properties that are most likely to be associated to understanding the fashion ontology. "
        "try to add atlist {num} properties including the name of product. "
        "Your response should be contain only a python list object nothing else."
    )

    attribute_list = list(attribute_dict.keys())

    prompt = prompt.format(attribute_list=attribute_list, num=len(attribute_list)//2)
    props = []
    for i in range(10):
        response = llm_response(prompt)
        if debug:
            print(f"Attempt {i+1}, ({response})")
        try:
            props = lo.get_list_from_response(response)
            break
        except:
            print("Error in get_list_from_response")
            continue
    
    properties = {}
    for prop in props:
        if prop in attribute_dict:
            if prop == 'sno':
                continue
            properties[prop] = attribute_dict[prop]

    return properties


