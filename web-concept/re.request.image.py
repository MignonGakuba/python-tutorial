import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://cdn.statically.io/img/i.pinimg.com/originals/bf/82/f6/bf82f6956a32819af48c2572243e8286.jpg")

print("Status code:", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Can not save the image")
