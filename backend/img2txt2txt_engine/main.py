import requests
import json
import helper as hp
import classification as cls
import load_ontology as lo
import os
from dotenv import load_dotenv
load_dotenv()

def img2txt2txt_engine():
    db_path_in = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/data_ingestion_engine/ingested_data.db'
    csv_path_in = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/data_ingestion_engine/ingested_data.csv'
    db_path_out = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/img2txt2txt_engine/extracted_data.db'
    ontology_path = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/ontology_engine/ONTOLOGY.json'
    i2t_model_endpoint = os.getenv("OLLAMA_URL")
    t2t_model_endpoint = i2t_model_endpoint

    raw_data = hp.read_db_file(db_path_in, 'ingested_data')
    # raw_data = hp.read_csv_file(csv_path_in)
    # make sure to change the range from raw_data[16:26] to raw_data only for final run
    for idx, data in enumerate(raw_data[17:25]):
        print(f"Iteration: {idx}, {type(data)}, {data[1]}")
        image_url = data[1]
        # image_caption = data[1]
        # try:
        if 1:
            image_description = image2text_model(image_url, i2t_model_endpoint)
            print(f"Image Description: {image_description}")
            hp.insert_into_db(db_path_out, 'extracted_data', image_url, '', image_description)
        # except:
        #     print("Error in image2text_model")
    print("Done for image2text_model")

    raw_data = hp.read_db_file(db_path_out, 'extracted_data')
    for idx, data in enumerate(raw_data):
        print(f"Iteration: {idx}")
        entity_id = data[0]
        image_description = data[3]
        try:
            style_attributes = text2text_model(image_description, t2t_model_endpoint)
            style_attributes = json.loads(style_attributes)
            hp.update_db_file_attributes(db_path_out, 'extracted_data', entity_id, style_attributes)
        except:
            print("Error in text2text_model")
    print("Done for text2text_model")

    raw_data = hp.read_db_file(db_path_out, 'extracted_data')
    for idx, data in enumerate(raw_data):
        print(f"Iteration: {idx}")
        entity_id = data[0]
        image_description = data[3]
        try:
            ontology = text2ontology_model(image_description, t2t_model_endpoint, ontology_path)
            hp.update_db_file_ontology(db_path_out, 'extracted_data', entity_id, ontology)
        except:
            print("Error in text2ontology_model")
    print("Done for text2ontology_model")

    print("ALL DONE")



def image2text_model(image_url, ollama_url, desci=None):
    prompt = """"Analyze the image provided, which contains an advertisement for a fashion product. "
    {description_caption}
    "Your task is to identify and describe only the main fashion item that is the focus of the advertisement. "
    "Ignore background elements, additional accessories, or other secondary items. "
    "Extract and describe the key style attributes of the identified product, such as color, material, pattern, fit, "
    "and unique design details. If relevant, include how the advertisement’s presentation enhances the product's appeal. "
    "Do not describe unrelated elements in the image—focus solely on the main fashion product being advertised."
    """

    description_caption = ""
    if desci:
        description_caption = f"Description: {desci}"
    
    prompt.format(description_caption=description_caption)
    encoded_image = hp.encode_image_to_base64(image_url)

    ollama_llama_url = f"{ollama_url}/api/chat"
    payload_llama = {
    "model": "llama3.2-vision",
    "messages": [
        {
        "role": "user",
        "content": prompt,
        "images": [encoded_image]
        }
    ]
    }

    response = requests.post(ollama_llama_url, data=json.dumps(payload_llama))
    print(response.text)
    return hp.get_output_text(response)


def text2text_model(input_text, ollama_url):
    instruction = "I have a product. Extract key style attributes from the provided product description and return them in a JSON dictionary format. Ensure the attributes are concise, relevant to fashion (e.g., color, pattern, fit, material), and avoid unnecessary information. The response should strictly follow the JSON format without any additional text."
    alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    {}

    ### Input:
    {}

    ### Response:
    {}"""
    eos_token = '<|end_of_text|>'
    text = alpaca_prompt.format(instruction, input_text, "") + eos_token

    ollama_llama_url = f"{ollama_url}/api/generate"
    payload_llama = {
        "model": "hf.co/ImJericho/model-t2t-stylumia-8bit",
        "prompt": text,
        "stream": False
    }

    response = requests.post(ollama_llama_url, data=json.dumps(payload_llama))
    return hp.get_output_text_v2(response)


def text2ontology_model(input_text, ollama_path, ontology_path):
    ontology = json.load(open(ontology_path))

    prompt = input_text
    # try:
    if 1:
        debug = False
        a, superclass = cls.get_existing_class_from_text_using_ollama(prompt, ontology['superclasses'], lo.get_class_defination('superclass'), debug)
        if superclass == "Home Decor":
            superclass = "Decor"
        elif a:
            superclass = "Clothing"
        b, class_t = cls.get_new_or_existing_class_from_text_using_ollama(prompt, ontology[superclass]['classes'], lo.get_class_defination('class'), debug, parent_classes=[superclass])
        if b:
            c, type_t = cls.get_new_class_from_text_using_ollama(prompt, lo.get_class_defination('type'), debug, parent_classes=[superclass, class_t])
            d, variant = cls.get_new_class_from_text_using_ollama(prompt, lo.get_class_defination('variant'), debug, parent_classes=[superclass, class_t, type_t])
            e, style = cls.get_new_class_from_text_using_ollama(prompt, lo.get_class_defination('style'), debug, parent_classes=[superclass, class_t, type_t])                    
        else:    
            c, type_t = cls.get_new_or_existing_class_from_text_using_ollama(prompt, ontology[superclass][class_t]['types'], lo.get_class_defination('type'), debug, parent_classes=[superclass, class_t])
            if c:
                d, variant = cls.get_new_class_from_text_using_ollama(prompt, lo.get_class_defination('variant'), debug, parent_classes=[superclass, class_t, type_t])
                e, style = cls.get_new_class_from_text_using_ollama(prompt, lo.get_class_defination('style'), debug, parent_classes=[superclass, class_t, type_t])
            else:
                d, variant = cls.get_new_or_existing_class_from_text_using_ollama(prompt, ontology[superclass][class_t][type_t]['variants'], lo.get_class_defination('variant'), debug, parent_classes=[superclass, class_t, type_t])
                e, style = cls.get_new_or_existing_class_from_text_using_ollama(prompt, ontology[superclass][class_t][type_t]['styles'], lo.get_class_defination('style'), debug, parent_classes=[superclass, class_t, type_t])

        if b:
            if 'classes' not in ontology[superclass]:
                ontology[superclass]['classes'] = [class_t]
            else:
                ontology[superclass]['classes'].append(class_t)
            ontology[superclass][class_t] = {}
            c=True
            d=True
            e=True
        if c:
            if 'types' not in ontology[superclass][class_t]:
                ontology[superclass][class_t]['types'] = [type_t]
            else:
                ontology[superclass][class_t]['types'].append(type_t)
            ontology[superclass][class_t][type_t] = {}
            d=True
            e=True
        if d:
            if 'variants' not in ontology[superclass][class_t][type_t]:
                ontology[superclass][class_t][type_t]['variants'] = [variant]
            else:
                ontology[superclass][class_t][type_t]['variants'].append(variant)
        if e:
            if 'styles' not in ontology[superclass][class_t][type_t]:
                ontology[superclass][class_t][type_t]['styles'] = [style]
            else:
                ontology[superclass][class_t][type_t]['styles'].append(style)

    ontology_dict = {
        "superclass": superclass,
        "class": class_t,
        "type": type_t,
        "variant": variant,
        "style": style
    }

    return ontology_dict
   

if __name__ == "__main__":
    db_path = '/Users/vivek/Drive E/Hackathons/Stylumia/stylumia-nxt/backend/img2txt2txt_engine/extracted_data.db'

    if os.path.exists(db_path):
        # hp.drop_db_file(db_path, 'extracted_data')
        pass
    else:
        hp.create_db_file(db_path, 'extracted_data')


    img2txt2txt_engine()
