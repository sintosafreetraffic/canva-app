import requests
import os
import json

# Ensure image folder exists
os.makedirs("product_images", exist_ok=True)

# Load image data from JSON file
with open("image_data.json", "r") as file:
    data = json.load(file)

image_urls = data["image_urls"]
product_names = data["product_names"]

# Download images
for i, url in enumerate(image_urls):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        filename = f"product_images/{product_names[i].replace(' ', '_')}.jpg"
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"✅ Downloaded: {os.path.abspath(filename)}")
    else:
        print(f"❌ Failed to download: {url}")
