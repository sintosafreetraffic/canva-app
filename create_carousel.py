from PIL import Image
import os

# Ensure carousel folder exists
os.makedirs("carousel_images", exist_ok=True)

# Resize images for carousel format
for i, image_path in enumerate(os.listdir("product_images")[:4]):
    image = Image.open(f"product_images/{image_path}").resize((1000, 1500))
    image.save(f"carousel_images/carousel_{i+1}.jpg")
    print(f"✅ Carousel image saved: carousel_{i+1}.jpg")
