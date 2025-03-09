import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# ✅ Google Sheets IDs
INPUT_SHEET_ID = "1SutOYJ0UA-DDy1d4Xf86jf4wh8-ImNG5Tq0lcvMlqmE"  # Where URLs are stored
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

# ✅ Open the correct sheet
sheet = client.open_by_key(INPUT_SHEET_ID).sheet1

# ✅ Fetch first 11 rows (Row 1 is header, so we take row 2-11)
data = sheet.get_all_values()[1:11]  # First 10 rows (excluding header)

# ✅ Extract Image URLs & Product Names
image_urls = [row[0].strip() for row in data if len(row) > 0 and row[0].startswith("http")]
product_names = [row[1].strip() if len(row) > 1 else "Unknown Product" for row in data]

# ✅ Debugging Output
if not image_urls:
    print("❌ No valid image URLs found in Google Sheets. Please check Column A format.")
else:
    print(f"✅ Retrieved {len(image_urls)} valid images from Google Sheets.")

# ✅ Save data
json_path = "image_data.json"
with open(json_path, "w") as file:
    json.dump({"image_urls": image_urls, "product_names": product_names}, file)

print(f"✅ Image data saved to: {json_path}")
