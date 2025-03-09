import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

# ✅ Google Sheets IDs
OUTPUT_SHEET_ID = "1IBUnoMB5FddHxZst-71LMwrwgS0t2joQPn7FZ9WwHOA"  # Where results are stored
SERVICE_ACCOUNT = "google_sheets_credentials.json"

# ✅ Authenticate with Google Sheets
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT, scope)
client = gspread.authorize(creds)

# ✅ Open the correct output sheet
sheet = client.open_by_key(OUTPUT_SHEET_ID).sheet1

# ✅ Load product names from JSON file
with open("image_data.json", "r") as file:
    data = json.load(file)

product_names = data["product_names"]

# ✅ Retrieve generated creatives
processed_files = sorted(os.listdir("processed_images"))

# ✅ Debugging: Check if creatives exist
print(f"✅ Found {len(processed_files)} creatives in: {os.path.abspath('processed_images')}")

# ✅ Upload creatives to the output sheet
for i, product in enumerate(product_names):
    row_index = i + 2  # Google Sheets rows start at 1, header is in row 1

    # ✅ Upload creatives (first 5 images per product)
    creatives = processed_files[i*5:(i+1)*5]  # 5 creatives per product
    image_links = [f"https://your-storage-url/{creative}" for creative in creatives]  # Replace with actual hosting link

    # ✅ Update the output sheet starting from Column J
    sheet.update(f"J{row_index}:X{row_index}", [image_links])

    print(f"✅ Uploaded creatives for {product} to Google Sheets (Row {row_index})")

print("✅ Google Sheets Updated Successfully!")
