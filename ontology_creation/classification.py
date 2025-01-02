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

def get_class_from_text_using_ollama(datapoint, class_list, class_defination, debug=False):
    prompt = (
        "You are tasked with classifying a fashion product based on the following description: {description}. "
        "Select the most appropriate class for this item from the list: {class_list}. This list represents classifications based on the class defination as {class_defination}. "
        "If the item does not fit any of the existing classes, generate a new class that best describes it, but remember if you are creating a new class then make sure it follows the class defination and it is generic to fit few other products in it. "
        "Respond with a JSON object containing only the key 'class' and the value as the determined class (from the list, a newly generated class)."
    )

    prompt = prompt.format(description=datapoint, class_list=class_list, class_defination=class_defination)
    

    for i in range(10):
        response = llm_response(prompt)
        if debug:
            print(f"Attempt {i+1}, ({response})")
        try:
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
        "try to add atleast {num} properties including the name of product. "
        "Your response should be contain only a json list of strings nothing else."
    )

    attribute_list = list(attribute_dict.keys())
    print(attribute_list)

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


