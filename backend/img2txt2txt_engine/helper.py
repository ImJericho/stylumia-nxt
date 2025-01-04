import base64
from PIL import Image
import io
import requests


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