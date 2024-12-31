import classification as cls
import load_ontology as lo
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pandas as pd



def filter_style_attributes(path, final_path, min_num_attributes=4):
    for filename in os.listdir(path):
        df = pd.read_csv(f'{path}/' + filename)
        new_df = pd.DataFrame(columns=df.columns)
        skip = 0
        for index, row in df.iterrows():
            i = row['style_attributes']
            i = i.replace("'", '"').encode('utf-8').decode('unicode_escape')
            try: 
                json_obj = json.loads(i)
            except:
                skip += 1
                continue
            if len(json_obj) < min_num_attributes:
                skip += 1
                continue
            df.at[index, 'style_attributes'] = i
            new_df = pd.concat([new_df, df.iloc[[index]]], ignore_index=True)    
        new_df.to_csv(f'{final_path}/{filename}', index=False)
        print(f"Saved {filename} with {skip} skipped rows out of {len(df)}")


def prepare_dataset_for_llm(path):
    prompt_input = ''' product_name: {product_name}
    description: {description}+{meta_info}
    feature_list: {feature_list}
    '''

    data = []
    wasted = 0
    total = 0

    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            print(f"Processing {filename}")
            df = pd.read_csv(f'{path}/{filename}')
            total_rows = len(df)
            total += total_rows
            for index, row in df.iterrows():
                product_name = row['product_name']
                description = row['description']
                meta_info = row['meta_info']
                feature_list = row['feature_list']
                prompt = prompt_input.format(product_name=product_name, description=description, meta_info=meta_info, feature_list=feature_list)
                
                ontology = json.load(open('ontology_dict.json'))

                # print(ontology['superclasses'])
                # _, superclass = cls.get_class_from_text_using_ollama(prompt, ontology['superclasses'])
                # print(superclass)
                # print(superclass[superclass]['subclasses'])
                # _, subclass = cls.get_class_from_text_using_ollama(prompt, superclass[superclass]['subclasses'])
                # print(subclass[superclass][subclass]['subsubclasses'])
                # _, subsubclass = cls.get_class_from_text_using_ollama(prompt, subclass[superclass][subclass]['subsubclasses'])
                # print(subsubclass[superclass][subclass][subsubclass]['category'])
                # _, category = cls.get_class_from_text_using_ollama(prompt, subsubclass[superclass][subclass][subsubclass]['category'])

                try:
                    a, superclass = cls.get_class_from_text_using_ollama(prompt, ontology['superclasses'], debug=False)
                    b, subclass = cls.get_class_from_text_using_ollama(prompt, ontology[superclass]['subclasses'], debug=False)
                    c, subsubclass = cls.get_class_from_text_using_ollama(prompt, ontology[superclass][subclass]['subsubclasses'], debug=False)
                    d, category = cls.get_class_from_text_using_ollama(prompt, ontology[superclass][subclass][subsubclass]['categories'], debug=False)
                    
                    # if a or b or c or d:
                    #     raise Exception("Error classifing found new class")
                except:
                    print(f"Error classifing row {index + 1} of {total_rows} in {filename}")
                    wasted += 1
                    continue


                ontology_dict = {
                    "superclass": superclass,
                    "subclass": subclass,
                    "subsubclass": subsubclass,
                    "category": category
                }

                compulsory_properties = {
                    "product_id": row['product_id']
                }

                properties = json.loads(row['style_attributes'])
                # try:
                #     properties = cls.get_filtered_properties_from_attribute(json.loads(row['style_attributes']), debug=False)
                # except:
                #     print(f"Error filtering row {index + 1} of {total_rows} in {filename}")
                #     wasted += 1
                #     continue

                combined_dict = {**properties, **ontology_dict}
                combined_dict2 = {**combined_dict, **compulsory_properties}
                data.append(combined_dict2)
                
                if index % 1 == 0:
                    print(f"Processed row {index + 1} of {total_rows} in {filename}")

                if index % 10 == 0:
                    with open(f'dataset/FINAL_READY_DATA.json', 'w') as f:
                        print("Saving chunk data")
                        json.dump(data, f)
    
        print("Finished processing", filename)
    print(f"Total wasted rows: {wasted} out of {total}")
    print("\n\n")
    print(f"Saving data to dataset/FINAL_READY_DATA.json")
    with open(f'dataset/FINAL_READY_DATA.json', 'w') as f:
        json.dump(data, f)

    return

                
def main():
    # filter_style_attributes('../data/processed_csv', 'dataset/processed_csv', min_num_attributes=0)
    prepare_dataset_for_llm('dataset/processed_csv')


if __name__ == "__main__":
    main()