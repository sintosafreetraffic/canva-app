from PIL import Image
import os  # ✅ FIXED: Added missing import statement

# Define collage format
collage_width, collage_height = 1000, 1500
grid_size = (2, 2)
img_size = (collage_width // grid_size[0], collage_height // grid_size[1])

# Ensure enough images are available
img_files = os.listdir("product_images")[:4]
if len(img_files) < 4:
    print("❌ Not enough images for a collage!")
else:
    collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))
    
    for idx, img_name in enumerate(img_files):
        img = Image.open(f"product_images/{img_name}").resize(img_size)
        x_offset = (idx % 2) * img_size[0]
        y_offset = (idx // 2) * img_size[1]
        collage.paste(img, (x_offset, y_offset))

    collage.save("processed_images/collage.jpg")
    print("✅ Collage Created!")
