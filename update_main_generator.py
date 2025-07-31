#!/usr/bin/env python3
"""
Add German and Spanish functions to the main CV generator
"""

# Read the German and Spanish functions from the add_de_es_cv.py file
with open('add_de_es_cv.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the German and Spanish functions
de_start = content.find('def generate_de_cv():')
es_start = content.find('def generate_es_cv():')
main_start = content.find('def main():')

de_function = content[de_start:es_start].strip()
es_function = content[es_start:main_start].strip()

# Read the main generator
with open('improved_cv_generator.py', 'r', encoding='utf-8') as f:
    main_content = f.read()

# Find where to insert the functions (after the Slovak function)
sk_end = main_content.find('def generate_sk_cv():')
sk_function_end = main_content.find('"""', sk_end + 100) + 3
sk_function_end = main_content.find('"""', sk_function_end) + 3

# Insert the German and Spanish functions
new_content = (
    main_content[:sk_function_end] +
    '\n\n' + de_function +
    '\n\n' + es_function +
    '\n' + main_content[sk_function_end:]
)

# Write the updated content
with open('improved_cv_generator.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ German and Spanish functions added to main generator!")
print("📄 Updated improved_cv_generator.py with all 4 languages")