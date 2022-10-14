"""
Download and change laptop wallpaper automatically
"""
# Libraries
import requests
import json
import PyWallpaper


# Open API
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Fetching the data from api with a GET request and storing response

response = requests.get(api_url)
content = response.content

# Decoding the content from bytes to string
decoded_content = content.decode('UTF-8')

# Convert string to JSON
dict_content = json.loads(decoded_content)

# Get image url from content
image_url = dict_content['url']

# Download the image
res = requests.get(image_url)

# Save the image
with open('apod.png', 'wb') as image:
    image.write(res.content)

# Set as wallpaper
PyWallpaper.change_wallpaper('apod.png')
