"""
Download and change laptop wallpaper automatically
"""
# Requests Libraray
import requests

# Open API
api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Fetching the data from api with a GET request and storing response

response = requests.get(api_url)
content = response.content

# Decoding the content from bytes to string
decoded_content = content.decode('UTF-8')

# Printing the content
print(decoded_content)
