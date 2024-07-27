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

import pandas as pd

# Load the two CSV files
file1 = 'combined_file.csv'
file2 = 'combined.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combine the two dataframes
combined_df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicate rows
unique_df = combined_df.drop_duplicates()

# Save the unique dataframe to a new CSV file
unique_df.to_csv('combined_file.csv', index=False)

print("Files combined and duplicates removed successfully!")