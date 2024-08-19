# import os
# import json

# def extract_text(data, key_filter=None):
#     """
#     Recursively extract text from a nested JSON structure.
#     Only includes the text from specified keys in `key_filter`.
#     """
#     texts = []
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if key_filter and key in key_filter:
#                 if isinstance(value, str):
#                     texts.append(value)
#                 elif isinstance(value, dict):  # For cases like "Texts" where nested dicts exist
#                     for sub_key, sub_value in value.items():
#                         if isinstance(sub_value, str):
#                             texts.append(sub_value)
#             elif isinstance(value, (dict, list)):
#                 texts.extend(extract_text(value, key_filter))
    
#     elif isinstance(data, list):
#         for item in data:
#             texts.extend(extract_text(item, key_filter))
    
#     return texts

# def process_books_folder(base_folder, keys_to_include):
#     all_texts = []
    
#     # Walk through the books folder and process each JSON file
#     for root, dirs, files in os.walk(base_folder):
#         for file_name in files:
#             if file_name.endswith('.json'):
#                 file_path = os.path.join(root, file_name)
                
#                 with open(file_path, 'r', encoding='utf-8') as json_file:
#                     try:
#                         data = json.load(json_file)
#                         extracted_texts = extract_text(data, keys_to_include)
#                         all_texts.extend(extracted_texts)
#                     except (UnicodeDecodeError, json.JSONDecodeError) as e:
#                         print(f"Error processing file {file_name}: {e}")
    
#     return all_texts

# def main():
#     # Path to the books folder
#     books_folder = r'C:\Users\karti\Unknown\ChatGita\data\books'  # Update this path
    
#     # Define the keys you want to extract text from
#     keys_to_include = {
#         'purport', 'Purport',
#         'text', 'Text', 'Texts',
#         'verseText', 'VerseText',
#         'chapterText', 'ChapterText',
#         'chaptercontent', 'Chaptercontent', 'chapterContent', 'ChapterContent',
#         'content', 'Content'
#     }
    
#     # Process all JSON files in the books folder
#     all_extracted_texts = process_books_folder(books_folder, keys_to_include)
    
#     # Combine all texts into a single string
#     combined_text = "\n\n".join(all_extracted_texts)
    
#     # Save the combined text to a file
#     output_file_path = 'extracted_text.txt'  # Update this path
#     with open(output_file_path, 'w', encoding='utf-8') as output_file:
#         output_file.write(combined_text)
    
#     print(f"Extracted text has been saved to {output_file_path}")

# if __name__ == "__main__":
#     main()


import os
import json

def extract_text(data, key_filter=None):
    """
    Recursively extract text from a nested JSON structure.
    Only includes the text from specified keys in `key_filter`.
    """
    texts = []
    
    if isinstance(data, dict):
        for key, value in data.items():
            if key_filter and key in key_filter:
                if isinstance(value, str):
                    texts.append(value)
                elif isinstance(value, list):  # Check if the value is a list of strings
                    for item in value:
                        if isinstance(item, str):
                            texts.append(item)
                elif isinstance(value, dict):  # Handle nested dictionaries (like "Texts")
                    texts.extend(extract_text(value, key_filter))
            elif isinstance(value, (dict, list)):
                texts.extend(extract_text(value, key_filter))
    
    elif isinstance(data, list):
        for item in data:
            texts.extend(extract_text(item, key_filter))
    
    return texts

def process_books_folder(base_folder, keys_to_include):
    all_texts = []
    
    # Walk through the books folder and process each JSON file
    for root, dirs, files in os.walk(base_folder):
        for file_name in files:
            if file_name.endswith('.json'):
                file_path = os.path.join(root, file_name)
                
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    try:
                        data = json.load(json_file)
                        extracted_texts = extract_text(data, keys_to_include)
                        all_texts.extend(extracted_texts)
                    except (UnicodeDecodeError, json.JSONDecodeError) as e:
                        print(f"Error processing file {file_name}: {e}")
    
    return all_texts

def main():
    # Path to the books folder
    books_folder = r'C:\Users\karti\Unknown\ChatGita\data\books'  # Update this path
    
    # Define the keys you want to extract text from
    keys_to_include = {
        'purport', 'Purport', 'purports', 'Purports',
        'text', 'Text', 'Texts', 'texts',
        'verseText', 'VerseText', 'verse_text', 'Verse_text',
        'chapterText', 'ChapterText', 'chapter_text', 'Chapter_text',
        'chaptercontent', 'Chaptercontent', 'chapterContent', 'ChapterContent',
        'content', 'Content', 'contents', 'Contents', 
        'Paragraphs', 'paragraphs', 'paragraph', 'Paragraph',
    }
    
    # Process all JSON files in the books folder
    all_extracted_texts = process_books_folder(books_folder, keys_to_include)
    
    # Combine all texts into a single string
    combined_text = "\n\n".join(all_extracted_texts)
    
    # Save the combined text to a file
    output_file_path = 'extracted_text1.txt'  # Update this path
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(combined_text)
    
    print(f"Extracted text has been saved to {output_file_path}")

if __name__ == "__main__":
    main()
