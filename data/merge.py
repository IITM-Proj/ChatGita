import os
import pandas as pd

def merge_csv_files(conversations_folder, output_file):
    all_dataframes = []

    for root, dirs, files in os.walk(conversations_folder):
        for file_name in files:
            if file_name.endswith('.csv'):
                file_path = os.path.join(root, file_name)
                try:
                    df = pd.read_csv(file_path)
                    all_dataframes.append(df)
                except Exception as e:
                    print(f"Error processing file {file_name}: {e}")

    if all_dataframes:
        merged_df = pd.concat(all_dataframes, ignore_index=True)

        merged_df.to_csv(output_file, index=False)
        print(f"All CSV files have been merged and saved to {output_file}")
    else:
        print("No CSV files found to merge.")

def main():
    conversations_folder = 'conversations'
    output_file = 'conversations.csv'
    merge_csv_files(conversations_folder, output_file)

if __name__ == "__main__":
    main()
