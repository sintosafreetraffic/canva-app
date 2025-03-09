from PIL import Image, ImageDraw, ImageFont
import os
import json
import random
import time

# ✅ Load product names
with open("image_data.json", "r") as file:
    data = json.load(file)

image_urls = data.get("image_urls", [])
product_names = data.get("product_names", [])

# ✅ Limit processing to 10 images max
image_urls = image_urls[:10]
product_names = product_names[:10]

# ✅ Ensure we have matching product names
if len(product_names) < len(image_urls):
    print(f"⚠ Warning: More images ({len(image_urls)}) than product names ({len(product_names)})!")
    for _ in range(len(image_urls) - len(product_names)):
        product_names.append("Unknown Product")

# ✅ Define template styles
TEMPLATES = [
    {"text": "🔥 Bestseller – Jetzt zugreifen!", "position": (50, 50), "color": "red"},
    {"text": "🚀 Trend des Jahres 2025!", "position": (50, 100), "color": "blue"},
    {"text": "💎 Limited Edition – Exklusiv erhältlich!", "position": (50, 150), "color": "green"},
    {"text": "🌟 Must-Have für deinen Style!", "position": (50, 200), "color": "purple"},
    {"text": "🎉 Nur für kurze Zeit!", "position": (50, 250), "color": "orange"}
]

# ✅ Ensure processed folder exists
os.makedirs("processed_images", exist_ok=True)

# ✅ Generate templates with progress tracking
print("\n🚀 Starting template generation...")
for i, img_name in enumerate(os.listdir("product_images")[:10]):
    if i >= len(product_names):
        print(f"⚠ Skipping {img_name}, no matching product name found!")
        continue

    img_path = os.path.join("product_images", img_name)
    product_img = Image.open(img_path).resize((1000, 1500))

    # ✅ Convert image to RGB to fix the RGBA JPEG issue
    if product_img.mode == "RGBA":
        product_img = product_img.convert("RGB")

    for j, template in enumerate(TEMPLATES):
        img_copy = product_img.copy()
        draw = ImageDraw.Draw(img_copy)
        font = ImageFont.load_default()

        draw.text(template["position"], template["text"], fill=template["color"], font=font)

        output_file = f"processed_images/{product_names[i].replace(' ', '_')}_template_{j+1}.jpg"
        img_copy.save(output_file, format="JPEG")

        print(f"✅ Processed {i+1}/10: {output_file}")
        time.sleep(0.2)  # Simulate slight delay for better progress visibility
print("\n✅ All templates generated successfully!")
