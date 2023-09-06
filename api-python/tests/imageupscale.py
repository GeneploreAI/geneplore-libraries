from geneplore_api import api_sync as api
import base64

api.api_key = ''


with open('image.png', 'rb') as f:
    bts = f.read()

image, cost = api.Image.Upscale(model="esrgan-v1-x2plus", image=bts)
with open('imageus.png', 'wb') as f:
    f.write(image)
    print(f"Image saved to image.png, cost: {cost}")