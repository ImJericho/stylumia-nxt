import base64
from PIL import Image
import io
import requests
import sqlite3
import re
import json
import csv
import pandas as pd

def create_db_file(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE {table_name} 
             (entity_id INTEGER PRIMARY KEY AUTOINCREMENT, image_url TEXT, image_caption TEXT, image_description TEXT, style_attributes TEXT, superclass TEXT, class TEXT, type TEXT, variant TEXT, style TEXT)''')
    conn.commit()
    conn.close()

def read_db_file(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def read_csv_file(csv_path):
    df = pd.read_csv(csv_path)
    image_urls = df['post_image_urls'].tolist()  
    return image_urls

#insert rows into the database
def insert_into_db(db_path, table_name, image_url, image_caption, image_description):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} (image_url, image_caption, image_description) VALUES (?, ?, ?)", (image_url, image_caption, image_description))
    conn.commit()
    conn.close()

def update_db_file_attributes(db_path, table_name, entity_id, style_attributes):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table_name} SET style_attributes = ? WHERE entity_id = ?", (style_attributes, entity_id))
    conn.commit()
    conn.close()

def update_db_file_ontology(db_path, table_name, entity_id, ontology):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table_name} SET superclass = ?, class = ?, type = ?, variant = ?, style = ? WHERE entity_id = ?", 
                   (ontology['superclass'], ontology['class'], ontology['type'], ontology['variant'], ontology['style'], entity_id))
    conn.commit()
    conn.close()

def get_image_from_url(image_url):
    response = requests.get(image_url, stream=True)
    image = Image.open(response.raw)
    return image

def encode_image_to_base64(image_url):
    image = get_image_from_url(image_url)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

#show image back from base64
def decode_image_from_base64(encoded_image):
    image = base64.b64decode(encoded_image)
    image = Image.open(io.BytesIO(image))
    #show this image in the new window
    image.show()
    return image

def get_output_text_v2(response):
    response_dict = response.json()
    response = response_dict['response']

    try:
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
        return json.dumps(match)
    except:
        return json.dumps(response)

def get_output_text(response):
    output_text = ""
    for line in response.text.splitlines():
        try:
            data = json.loads(line)
            if 'message' in data and 'content' in data['message']:
                output_text += data['message']['content']
        except json.JSONDecodeError:
            pass
        output_text = output_text.replace("*", "")
    return output_text