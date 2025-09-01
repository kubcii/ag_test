#!/usr/bin/env python3
"""
Integrate the real professional photo into all CV and portfolio websites
"""

import os
import base64

def convert_image_to_base64(image_path):
    """Convert image file to base64 data URL"""
    try:
        with open(image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    except Exception as e:
        print(f"Error converting image: {e}")
        return None

def create_photo_css():
    """Create enhanced CSS for photo integration"""
    return """
        .profile-photo {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid white;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            margin: 20px auto;
            display: block;
        }
        
        .header-with-photo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        
        .header-text {
            text-align: center;
        }
        
        @media (max-width: 768px) {
            .header-with-photo {
                flex-direction: column;
                gap: 20px;
            }
            .profile-photo {
                width: 120px;
                height: 120px;
            }
        }
        
        @media (max-width: 480px) {
            .profile-photo {
                width: 100px;
                height: 100px;
            }
        }
    """

def update_html_files():
    """Update all HTML files with the real photo"""
    # Convert the image to base64
    photo_base64 = convert_image_to_base64('image.png')
    
    if not photo_base64:
        print("❌ Failed to convert image")
        return
    
    photo_css = create_photo_css()
    
    # List of all HTML files to update
    html_files = [
        'improved_cv_en_v4.html',
        'improved_cv_sk_v4.html', 
        'improved_cv_de_v4.html',
        'improved_cv_es_v4.html',
        'portfolio.html',
        'ski-technician.html'
    ]
    
    for filename in html_files:
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace placeholder photo with real photo
                placeholder_pattern = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD'
                if placeholder_pattern in content:
                    # Find and replace the entire placeholder data URL
                    start_idx = content.find('data:image/jpeg;base64,')
                    if start_idx != -1:
                        end_idx = content.find('"', start_idx)
                        if end_idx != -1:
                            old_data_url = content[start_idx:end_idx]
                            content = content.replace(old_data_url, photo_base64)
                
                # Ensure photo CSS is present
                if '.profile-photo {' not in content:
                    content = content.replace('</style>', photo_css + '\n    </style>')
                
                # Ensure photo HTML structure is present
                if 'header-with-photo' not in content:
                    # Add photo structure for different file types
                    if 'Alpine Skiing Coach' in content:
                        photo_html = f'''
            <div class="header-with-photo">
                <img src="{photo_base64}" alt="Andrej Gyure" class="profile-photo">
                <div class="header-text">
                    <h1>Andrej Gyure</h1>
                    <h2>Alpine Skiing Coach</h2>
                </div>
            </div>'''
                        content = content.replace('<h1>Andrej Gyure</h1>\n            <h2>Alpine Skiing Coach</h2>', photo_html)
                    
                    elif 'Elite Alpine Skiing Coach' in content:
                        photo_html = f'''
            <div class="header-with-photo">
                <img src="{photo_base64}" alt="Andrej Gyure" class="profile-photo">
                <div class="header-text">
                    <h1>Andrej Gyure</h1>
                    <h2>Elite Alpine Skiing Coach</h2>
                </div>
            </div>'''
                        content = content.replace('<h1>Andrej Gyure</h1>\n            <h2>Elite Alpine Skiing Coach</h2>', photo_html)
                    
                    elif 'Ski Technician & Professional Trainer' in content:
                        photo_html = f'''
            <div class="header-with-photo">
                <img src="{photo_base64}" alt="Andrej Gyure" class="profile-photo">
                <div class="header-text">
                    <h1>Andrej Gyure</h1>
                    <h2>Ski Technician & Professional Trainer</h2>
                </div>
            </div>'''
                        content = content.replace('<h1>Andrej Gyure</h1>\n            <h2>Ski Technician & Professional Trainer</h2>', photo_html)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✅ Updated {filename} with professional photo")
                
            except Exception as e:
                print(f"❌ Error updating {filename}: {e}")

def main():
    """Main function to integrate the real photo"""
    print("🖼️  Integrating your professional photo into all websites...")
    print("📸 Converting image.png to base64...")
    
    # Update all HTML files
    update_html_files()
    
    print("\n✅ Photo integration complete!")
    print("📄 Updated files:")
    print("   - All CV versions (EN/SK/DE/ES)")
    print("   - Portfolio website")
    print("   - Ski technician services")
    print("\n🎨 Features:")
    print("   - High-quality professional photo")
    print("   - Responsive circular design")
    print("   - Mobile-optimized display")
    print("   - Consistent across all pages")
    print("\n🌐 Your websites now feature your professional photo!")

if __name__ == "__main__":
    main()
