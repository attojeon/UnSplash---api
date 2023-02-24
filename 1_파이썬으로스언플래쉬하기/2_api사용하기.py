import requests 
from PIL import Image
import matplotlib.pyplot as plt

url = "https://unsplash.com/napi/search/photos?query=cat&xp=&per_page=2&page=1"

total = 0
total_page = 0
response = requests.get(url)
if response.status_code == 200:
    photos = response.json()
    total = photos["total"]
    total_page = photos["total_pages"]

    print("Total:", total)
    print("Total Page:", total_page)
    for photo in photos["results"]:
        img_url = photo["urls"]["regular"]
        response = requests.get(img_url, stream=True)
        img = Image.open(response.raw)
        plt.imshow(img)
        plt.show()
    
else:
    print("Error Code:", response.status_code)
