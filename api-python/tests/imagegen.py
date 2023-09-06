from geneplore_api import api_sync as api

api.api_key = ''

image, cost = api.Image.Generate("damo", "A painting of a cat")
with open('image.png', 'wb') as f:
    f.write(image)
    print(f"Image saved to image.png, cost: {cost}")