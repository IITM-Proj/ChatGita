# import pandas as pd

# # Load the CSV file
# df = pd.read_csv('combined.csv', encoding='utf-8')

# # Function to clean the 'answer' text
# def clean_answer(text):
#     if isinstance(text, str):
#         # Remove "Prabhupāda:" and any leading/trailing whitespace
#         return text.replace('Prabhupāda:', '').strip()
#     return text

# # Apply the cleaning function to the 'answer' column
# df['answer'] = df['answer'].apply(clean_answer)

# # Save the cleaned DataFrame back to the CSV file
# df.to_csv('combined.csv', index=False, encoding='utf-8')

# print("Data cleaned and saved to 'conversation_cleaned.csv'")


# import pandas as pd

# # Load the two CSV files
# file1 = 'conversation_combined.csv'
# file2 = 'formatted_qa.csv'

# df1 = pd.read_csv(file1)
# df2 = pd.read_csv(file2)

# # Combine the two dataframes
# combined_df = pd.concat([df1, df2], ignore_index=True)

# # Save the combined dataframe to a new CSV file
# combined_df.to_csv('combined_file.csv', index=False)

# print("Files combined successfully!")

# import pandas as pd

# # Load the two CSV files
# file1 = 'combined_file.csv'
# file2 = 'combined.csv'

# df1 = pd.read_csv(file1)
# df2 = pd.read_csv(file2)

# # Combine the two dataframes
# combined_df = pd.concat([df1, df2], ignore_index=True)

# # Remove duplicate rows
# unique_df = combined_df.drop_duplicates()

# # Save the unique dataframe to a new CSV file
# unique_df.to_csv('combined_file.csv', index=False)

# print("Files combined and duplicates removed successfully!")

#############################################################################################

# Cleaning the output json file to ensure that response2 and response3 are not empty

# import json

# def clean_json_responses(input_path, output_path):
#     # Open and load the JSON file
#     with open(input_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     # Iterate through the data
#     for item in data:
#         response1 = item.get('response1', '')
#         response2 = item.get('response2', '')
#         response3 = item.get('response3', '')

#         # Check conditions and update responses
#         if not response2 and response3:
#             item['response2'] = response3
#         elif not response3 and response2:
#             item['response3'] = response2
#         elif not response2 and not response3:
#             item['response2'] = response1
#             item['response3'] = response1

#     # Save the cleaned JSON to the output file
#     with open(output_path, 'w', encoding='utf-8') as file:
#         json.dump(data, file, indent=4)

# # Provide the input and output file paths
# input_path = r'C:\Users\karti\Unknown\ChatGita\outputs\output.json'
# output_path = r'C:\Users\karti\Unknown\ChatGita\outputs\output_cleaned.json'

# # Call the function to clean the JSON
# clean_json_responses(input_path, output_path)

#############################################################################################

# Converting the cleaned JSON file to Alpaca format

import json

def convert_to_alpaca_format(input_path, output_path):
    # Open and load the JSON file
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Create a list to store the Alpaca-formatted data
    alpaca_data = []

    # Iterate through the data and transform it into Alpaca format
    for item in data:
        alpaca_item = {
            "instruction": item.get('instruction', ''),
            "input": item.get('input', ''),
            "output": item.get('response1', '')
        }
        alpaca_data.append(alpaca_item)

    # Save the Alpaca formatted data to the output file
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(alpaca_data, file, indent=4)

# Provide the input and output file paths
input_path = r'C:\Users\karti\Unknown\ChatGita\outputs\output_cleaned.json'
output_path = r'C:\Users\karti\Unknown\ChatGita\outputs\alpaca_formatted_file.json'

# Call the function to convert the JSON to Alpaca format
convert_to_alpaca_format(input_path, output_path)