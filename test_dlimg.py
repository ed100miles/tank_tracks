import requests

img_data = requests.get('https://pbs.twimg.com/media/FMDT8XPX0AIeOTK?format=jpg&name=900x900').content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)
