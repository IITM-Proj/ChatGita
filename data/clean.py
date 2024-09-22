import pandas as pd
import ollama

# Define a function to generate prompts and get model responses
def clean_conversation(row):
    prompt = f"""
    Clean the following conversation based on these rules:

    1. One-word answers: If an answer is a single word (e.g., 'yes', 'no', 'okay', 'sure') and does not add value to the conversation, remove it.
    2. Questions answered with a question: If the answer is a question and not contextually relevant, remove it.
    3. Short, non-informative answers: If the answer lacks useful information (e.g., 'I don't know', 'maybe'), remove it.
    4. Maintain context: Do not modify valid answers that make sense in the conversation.
    5. Keep about 60-80% of the conversation as is.
    
    Conversation:
    Question Speaker: {row['Question Speaker']}
    Question: {row['Question Text']}
    Answer Speaker: {row['Answer Speaker']}
    Answer: {row['Answer Text']}
    
    Based on these rules, provide the cleaned conversation with both question and answer.
    """

    response = ollama.generate(
        model="llama3.1-70B",  # Use the llama 3.1-70B model
        prompt=prompt
    )

    return response['text'].strip()

def process_conversations(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    cleaned_data = []
    
    for _, row in df.iterrows():
        cleaned_conversation = clean_conversation(row)
        
        if cleaned_conversation:
            cleaned_data.append({
                'Question Speaker': row['Question Speaker'],
                'Question Text': row['Question Text'],
                'Answer Speaker': row['Answer Speaker'],
                'Answer Text': cleaned_conversation
            })

    cleaned_df = pd.DataFrame(cleaned_data)
    cleaned_df.to_csv(output_csv, index=False)
    print(f"Cleaned conversation data saved to {output_csv}")

# Example usage
input_csv = "conversations.csv" 
output_csv = "cleaned_conversations.csv" 
process_conversations(input_csv, output_csv)
