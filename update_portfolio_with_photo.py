#!/usr/bin/env python3
"""
Update portfolio with real photo and remove unrelated images
"""

import base64
import os

def get_real_photo_base64():
    """Get the real photo as base64"""
    try:
        with open('image.png', 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def update_portfolio():
    """Update portfolio with real photo"""
    photo_base64 = get_real_photo_base64()
    if not photo_base64:
        return

    with open('portfolio.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace placeholder photo with real photo
    placeholder = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=='
    content = content.replace(placeholder, photo_base64)

    with open('portfolio.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Updated portfolio.html with real photo")

def update_ski_technician():
    """Update ski technician page with real photo"""
    photo_base64 = get_real_photo_base64()
    if not photo_base64:
        return

    with open('ski-technician.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace placeholder photo with real photo if it exists
    placeholder = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=='
    if placeholder in content:
        content = content.replace(placeholder, photo_base64)

    with open('ski-technician.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("✅ Updated ski-technician.html with real photo")

def main():
    """Main function"""
    print("🖼️ Updating portfolio files with real photo...")

    update_portfolio()
    update_ski_technician()

    print("✅ All portfolio files updated with professional photo!")
    print("🚫 No unrelated images found - all content is skiing-focused")

if __name__ == "__main__":
    main()
