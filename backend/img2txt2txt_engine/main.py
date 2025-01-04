import requests
import json



def img2txt2txt_engine():
    



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
    encoded_image = encode_image_to_base64(image_url)

    ollama_llava_url = f"{ollama_url}/api/generate"
    payload_llava = {
    "model": "llava:13b",
    "prompt":prompt,
    "stream": False,
    "image": [encoded_image]
    }

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

    return get_output_text(response)




if __name__ == "__main__":
    image_url = "https://assets.stylumia.com/originals/2024/11/401/0420777b7addf5b98b915c71ced2f2109abc7f3deefaf38a732cb381de680d67.jpg"
    ollama_url = "https://310c-34-74-47-153.ngrok-free.app"

    print(image2text_model(image_url, ollama_url))