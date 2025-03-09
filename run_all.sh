#!/bin/bash

echo "🚀 Starting full automation process..."

# Step 1: Fetch product image URLs from Google Sheets
echo "🔄 Fetching image URLs..."
python3 fetch_images.py || { echo "❌ Failed to fetch images"; exit 1; }

# Step 2: Download the images
echo "📥 Downloading images..."
python3 download_images.py || { echo "❌ Failed to download images"; exit 1; }

# Step 3: Generate ad creatives
echo "🎨 Generating ad templates..."
python3 generate_templates.py || { echo "❌ Failed to generate templates"; exit 1; }

# Step 4: Create carousel ads
echo "📱 Creating carousel creatives..."
python3 create_carousel.py || { echo "❌ Failed to create carousels"; exit 1; }

# Step 5: Create image collages
echo "🖼 Generating multi-image collages..."
python3 create_collage.py || { echo "❌ Failed to create collages"; exit 1; }

# Step 6: Upload creatives to Google Sheets
echo "📤 Uploading creatives to Google Sheets..."
python3 create_google_sheet.py || { echo "❌ Failed to upload to Google Sheets"; exit 1; }

echo "✅ All steps completed successfully!"
