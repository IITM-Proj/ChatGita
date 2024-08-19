import os
import json

def get_json_schema(json_data):
    """Generate a schema from a JSON object."""
    if isinstance(json_data, dict):
        schema = {}
        for key, value in json_data.items():
            schema[key] = get_json_schema(value)
        return schema
    elif isinstance(json_data, list):
        if len(json_data) > 0:
            return [get_json_schema(json_data[0])]
        else:
            return []
    else:
        return type(json_data).__name__

def explore_books_folder(base_folder):
    folder_structure = {}

    for root, dirs, files in os.walk(base_folder):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            folder_structure[dir_name] = {}

            for file_name in os.listdir(folder_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(folder_path, file_name)
                    
                    try:
                        with open(file_path, 'r', encoding='utf-8') as json_file:
                            json_data = json.load(json_file)
                            schema = get_json_schema(json_data)
                            folder_structure[dir_name][file_name] = schema
                    except UnicodeDecodeError:
                        print(f"Encoding error in file: {file_name}")
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON from file: {file_name}")

    return folder_structure

# Example usage
books_folder = r'C:\Users\karti\Unknown\ChatGita\data\books'  # Update this path
folder_structure = explore_books_folder(books_folder)

# Convert the folder structure and schema to JSON format
folder_structure_json = json.dumps(folder_structure, indent=4)

output_file_path = 'schema.json'  # Update this path

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(folder_structure_json)
