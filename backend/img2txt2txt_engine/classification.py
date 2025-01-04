import json
import re
from sentence_transformers import SentenceTransformer, util
from ollama import chat
from ollama import ChatResponse
import load_ontology as lo
import os
import pandas as pd
import helper as hp
import requests
from dotenv import load_dotenv
load_dotenv()



def llm_response(msg, model='llama3.2'):
    ollama_url = os.getenv('OLLAMA_URL')
    print(ollama_url)
    url = f"{ollama_url}/api/generate"
    payload = {
        "model": model,
        "prompt": msg,
        "stream": False
    }
    response = requests.post(url, json=payload)
    return response.json()['response']    

def get_existing_class_from_text_using_ollama(datapoint, class_list, class_defination, debug=False, parent_classes=None):
    prompt = (
        "Classify a fashion product based on the following product description: {description}. "
        "{parent_classes_prompt}"
        "Select the most appropriate class for this item from the list: {class_list}. This list represents classifications based on the class defination as {class_defination}. "
        "Respond with a JSON object containing only one key 'class' and the value as the determined class (must be from the given list list)."
    )

    if parent_classes:
        parent_class_prompt = "The product is already a part of the following tags: {parent_classes}.".format(parent_classes=parent_classes)
    else:
        parent_class_prompt = ""
    prompt = prompt.format(description=datapoint, class_list = class_list, parent_classes_prompt=parent_class_prompt, class_defination=class_defination)
    json_obj = {}
    for i in range(5):
        response = llm_response(prompt)
        if debug:
            print(f"Attempt {i+1}, ({response})")
        try:
            json_obj = lo.get_json_from_response(response)
            break
        except:
            if debug:
                print("Error in lo.get_json_from_response")
            continue
    
    if json_obj['class'] not in class_list:
        if debug:
            print(f"Invalid class: {json_obj['class']}")
        return True, json_obj['class']
    
    if debug:
        print(f"Valid class: {json_obj['class']}")
    return False, json_obj['class']

def get_new_class_from_text_using_ollama(datapoint, class_defination, debug=False, parent_classes=None):
    prompt = (
        "Classify a fashion product based on the following product description: {description}. "
        "{parent_classes_prompt}"
        "Assign a new tag to this product based on the class defination: {class_defination}. "
        "Respond with a JSON object containing only one key 'class' and the value as the determined class."
    )
    if parent_classes:
        parent_class_prompt = "The product is already a part of the following tags: {parent_classes}.".format(parent_classes=parent_classes)
    else:
        parent_class_prompt = ""
    prompt = prompt.format(description=datapoint, parent_classes_prompt=parent_class_prompt, class_defination=class_defination)

    for i in range(5):
        response = llm_response(prompt)
        if debug:
            print(f"Attempt {i+1}, ({response})")
        try:
            json_obj = lo.get_json_from_response(response)
            break
        except:
            if debug:
                print("Error in lo.get_json_from_response")
            continue
    
    if debug:
        print(f"Valid class: {json_obj['class']}")
    return False, json_obj['class']

def get_new_or_focus_on_existing_class_from_text_using_ollama(datapoint, class_list, class_defination, debug=False, parent_classes=None):
    prompt = (
        "Classify a fashion product based on the following product description: {description}."
        "{parent_classes_prompt}"
        "Select the most appropriate class for this item from the list: {class_list}. This list represents classifications based on the defination: {class_defination}. "
        "If and only if there is no element in the given list that even slightly matches the given product, generate a new class that best describes it. However, if you create a new class, ensure that it follows the class definition and is general enough to apply to other similar products."
        "Respond with a JSON object containing only the key 'class' and the value as the determined class (from the list, a newly generated class)."
    )
    if parent_classes:
        parent_class_prompt = "The product is already a part of the following tags: {parent_classes}.".format(parent_classes=parent_classes)
    else:
        parent_class_prompt = ""

    prompt = prompt.format(description=datapoint, class_list=class_list, class_defination=class_defination, parent_classes_prompt=parent_class_prompt)
    

    for i in range(5):
        response = llm_response(prompt)
        if debug:
            print(f"Attempt {i+1}, ({response})")
        try:
            json_obj = lo.get_json_from_response(response)
            break
        except:
            if debug:
                print("Error in lo.get_json_from_response")
            continue
    
    if json_obj['class'] not in class_list:
        if debug:
            print(f"Invalid class: {json_obj['class']}")
        return True, json_obj['class']
    
    if debug:
        print(f"Valid class: {json_obj['class']}")
    return False, json_obj['class']

def get_new_or_existing_class_from_text_using_ollama(datapoint, class_list, class_defination, debug=False, parent_classes=None):
    prompt = (
        "Classify a fashion product based on the following product description: {description}. "
        "{parent_classes_prompt}"
        "Select the most appropriate class for this item from the list: {class_list}. This list represents classifications based on the class defination as {class_defination}. "
        "If the item does not fit any of the existing classes, generate a new class that best describes it, but remember if you are creating a new class then make sure it follows the class defination and it is generic to fit few other products in it. "
        "Respond with a JSON object containing only the key 'class' and the value as the determined class (from the list, a newly generated class)."
    )
    if parent_classes:
        parent_class_prompt = "The product is already a part of the following tag so avoid using them again: {parent_classes}".format(parent_classes=parent_classes)
    else:
        parent_class_prompt = ""

    prompt = prompt.format(description=datapoint, class_list=class_list, class_defination=class_defination, parent_classes_prompt=parent_class_prompt)
    

    for i in range(5):
        response = llm_response(prompt)
        if debug:
            print(f"Attempt {i+1}, ({response})")
        try:
            json_obj = lo.get_json_from_response(response)
            break
        except:
            if debug:
                print("Error in lo.get_json_from_response")
            continue
    
    if json_obj['class'] not in class_list:
        if debug:
            print(f"Invalid class: {json_obj['class']}")
        return True, json_obj['class']
    
    if debug:
        print(f"Valid class: {json_obj['class']}")
    return False, json_obj['class']


if __name__ == '__main__':

    print(llm_response("who are you? in short "))