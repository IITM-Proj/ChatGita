# import requests
# import time
# from bs4 import BeautifulSoup
# import json
# import os

# # Base URL for the chapters of "Perfect Questions, Perfect Answers"
# base_url = "https://vedabase.io/en/library/pqpa/{}/"

# # Headers to include in the request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9'
# }

# # Number of chapters in the book
# chapters_in_book = 9  # There are 9 chapters in the book

# # Dictionary to store the content for the book
# book_content = {}

# # Function to fetch a chapter with retries
# def fetch_chapter_with_retries(chapter_url, retries=5, backoff_factor=1.0):
#     for i in range(retries):
#         try:
#             response = requests.get(chapter_url, headers=headers)
#             response.raise_for_status()  # Raise an HTTPError for bad responses
#             return response
#         except requests.exceptions.RequestException as e:
#             print(f"Error fetching {chapter_url}: {e}")
#             if i < retries - 1:
#                 sleep_time = backoff_factor * (2 ** i)
#                 print(f"Retrying in {sleep_time} seconds...")
#                 time.sleep(sleep_time)
#             else:
#                 print(f"Failed to retrieve {chapter_url} after {retries} attempts.")
#                 return None

# # Loop through chapters 1 to the last chapter
# for chapter_number in range(1, chapters_in_book + 1):
#     chapter_url = base_url.format(chapter_number)
#     print(f"Fetching Chapter {chapter_number} from {chapter_url}")
    
#     response = fetch_chapter_with_retries(chapter_url)
    
#     if response is not None and response.status_code == 200:
#         # Parse the HTML content of the webpage
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Extract the chapter title
#         chapter_title_div = soup.find('div', class_='r-chapter-title')
#         chapter_title = chapter_title_div.get_text(strip=True) if chapter_title_div else f"Chapter {chapter_number}"
        
#         # Extract the paragraphs within the specified div
#         paragraphs = soup.find_all('div', class_='r r-lang-en r-paragraph')
        
#         # Extract the questions and answers
#         questions_answers = []
#         current_question = None
#         current_answer = None
        
#         for paragraph in paragraphs:
#             strong_tag = paragraph.find('strong')
#             if strong_tag:
#                 speaker = strong_tag.get_text(strip=True)
#                 text = paragraph.find('p').get_text(strip=True).replace(f"{speaker}: ", "")
#                 if speaker != "Śrīla Prabhupāda":
#                     if current_question:
#                         questions_answers.append(current_question)
#                     current_question = {'question': text, 'answer': ""}
#                 else:
#                     if current_question:
#                         current_question['answer'] += text + " "
        
#         if current_question:
#             questions_answers.append(current_question)
        
#         # Save the chapter title and questions/answers in the dictionary
#         book_content[str(chapter_number)] = {
#             'chapter_title': chapter_title,
#             'questions_answers': questions_answers
#         }
        
#         print(f"Chapter {chapter_number} fetched successfully.")
    
#     else:
#         print(f"Failed to retrieve Chapter {chapter_number}.")
    
#     # Delay between requests to avoid overloading the server
#     time.sleep(3)

# # Save the collected data to a JSON file
# output_dir = 'perfect_questions_perfect_answers'
# os.makedirs(output_dir, exist_ok=True)

# with open(os.path.join(output_dir, 'book_content.json'), 'w', encoding='utf-8') as f:
#     json.dump(book_content, f, ensure_ascii=False, indent=4)

# print(f"Data saved to '{output_dir}/book_content.json'")


# import json

# # Load the JSON data
# with open(r'C:\Users\karti\Unknown\FineTuning\perfect_questions_perfect_answers\\book_content.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # Initialize an empty list to store the formatted Q&A
# formatted_qa = []

# # Loop through each chapter and questions_answers pair
# for chapter in data.values():
#     questions_answers = chapter['questions_answers']
#     question = None
#     answer = None
#     for qa in questions_answers:
#         if qa['question'].startswith('Bob:') or qa['question'].startswith('Guest:') or qa['question'].startswith('Brahmānanda:'):
#             if question and answer:
#                 formatted_qa.append({"question": question, "answer": answer})
#             question = qa['question'].split(":", 1)[1].strip()
#             answer = None
#         elif qa['question'].startswith('Śrīla Prabhupāda:'):
#             answer = qa['question'].split(":", 1)[1].strip()

#     # Append the last Q&A pair
#     if question and answer:
#         formatted_qa.append({"question": question, "answer": answer})


# # Save the formatted Q&A to a new JSON file
# with open(r'C:\Users\karti\Unknown\FineTuning\perfect_questions_perfect_answers\\formatted_qa.json', 'w', encoding='utf-8') as file:
#     json.dump(formatted_qa, file, indent=4)

# # Print formatted Q&A to check
# for qa in formatted_qa:
#     print(f"Q: {qa['question']}")
#     print(f"A: {qa['answer']}\n")


# import pandas as pd
# import json

# # Load the JSON data
# with open(r'C:\Users\karti\Unknown\FineTuning\perfect_questions_perfect_answers\\book_content.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # Initialize an empty list to store the formatted Q&A
# formatted_qa = []

# # Loop through each chapter and questions_answers pair
# for chapter in data.values():
#     questions_answers = chapter['questions_answers']
#     question = None
#     answer = None
#     for qa in questions_answers:
#         if qa['question'].startswith('Bob:') or qa['question'].startswith('Guest:') or qa['question'].startswith('Brahmānanda:'):
#             if question and answer:
#                 formatted_qa.append({"question": question, "answer": answer})
#             question = qa['question'].split(":", 1)[1].strip()
#             answer = None
#         elif qa['question'].startswith('Śrīla Prabhupāda:'):
#             answer = qa['question'].split(":", 1)[1].strip()

#     # Append the last Q&A pair
#     if question and answer:
#         formatted_qa.append({"question": question, "answer": answer})

# # Convert the formatted Q&A list to a DataFrame
# qa_df = pd.DataFrame(formatted_qa)

# # Save the DataFrame to a CSV file
# output_csv_path = 'formatted_qa.csv'
# qa_df.to_csv(output_csv_path, index=False)

# qa_df.head()





# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # URL of the webpage
# url = "https://prabhupadabooks.com/conversations/1967/apr/discourse_on_lord_caitanya_play_between_srila_prabhupada_and_hayagriva/san_francisco/april/05/1967?d=1"

# # Headers to include in the request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9'
# }

# # Send a GET request to the URL
# response = requests.get(url, headers=headers)
# response.raise_for_status()

# # Parse the HTML content of the webpage
# soup = BeautifulSoup(response.text, 'html.parser')

# # Initialize lists to store the questions and answers
# questions = []
# answers = []

# # Extract the conversation
# conversation_divs = soup.find_all('div', class_='Purp-para')

# current_question = None
# current_answer = ""

# for div in conversation_divs:
#     bold_tag = div.find('span', class_='Bold')
#     if bold_tag:
#         speaker_tag = bold_tag.find('a')
#         speaker = speaker_tag.get_text(strip=True) if speaker_tag else bold_tag.get_text(strip=True)
#         text = div.get_text(strip=True).replace(f"{speaker}:", "").strip()
        
#         if speaker == "Prabhupāda:":
#             if current_question:
#                 current_answer += " " + text
#             else:
#                 current_answer = text
#         else:
#             if current_question and current_answer:
#                 questions.append(current_question)
#                 answers.append(current_answer.strip())
#             current_question = text
#             current_answer = ""

# if current_question and current_answer:
#     questions.append(current_question)
#     answers.append(current_answer.strip())

# # Create a DataFrame from the extracted data
# df = pd.DataFrame({
#     'question': questions,
#     'answer': answers
# })

# # Save the DataFrame to a CSV file
# df.to_csv('conversation.csv', index=False, encoding='utf-8')

# print("Data saved to 'conversation.csv'")


# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # URL of the webpage
# url = "https://prabhupadabooks.com/conversations/1967/apr/discourse_on_lord_caitanya_play_between_srila_prabhupada_and_hayagriva/san_francisco/april/05/1967?d=1"

# # Headers to include in the request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9'
# }

# # Send a GET request to the URL
# response = requests.get(url, headers=headers)
# response.raise_for_status()

# # Parse the HTML content of the webpage
# soup = BeautifulSoup(response.text, 'html.parser')

# # Initialize lists to store the questions and answers
# questions = []
# answers = []

# # Extract the conversation
# conversation_divs = soup.find_all('div', class_='Purp-para')

# current_question = None
# current_answer = ""

# for div in conversation_divs:
#     bold_tag = div.find('span', class_='Bold')
#     if bold_tag:
#         speaker_tag = bold_tag.find('a')
#         speaker = speaker_tag.get_text(strip=True) if speaker_tag else bold_tag.get_text(strip=True)
#         text = div.get_text(strip=True).replace(f"{speaker}:", "").strip()
        
#         if speaker == "Prabhupāda:":
#             if current_question:
#                 current_answer += " " + text
#             else:
#                 current_answer = text
#         else:
#             if current_question and current_answer:
#                 questions.append(current_question)
#                 answers.append(current_answer.strip())
#             current_question = text
#             current_answer = ""

# if current_question and current_answer:
#     questions.append(current_question)
#     answers.append(current_answer.strip())

# # Create a DataFrame from the extracted data
# df = pd.DataFrame({
#     'question': questions,
#     'answer': answers
# })

# # Save the DataFrame to a CSV file
# df.to_csv('conversation.csv', index=False, encoding='utf-8')

# print("Data saved to 'conversation.csv'")

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# List of URLs
urls = [
    'https://prabhupadabooks.com/conversations/1967/apr?d=1',
    'https://prabhupadabooks.com/conversations/1968/feb?d=1',
    'https://prabhupadabooks.com/conversations/1968/mar?d=1',
    'https://prabhupadabooks.com/conversations/1969/jan?d=1',
    'https://prabhupadabooks.com/conversations/1969/feb?d=1',
    'https://prabhupadabooks.com/conversations/1969/mar?d=1',
    'https://prabhupadabooks.com/conversations/1969/apr?d=1',
    'https://prabhupadabooks.com/conversations/1969/may?d=1',
    'https://prabhupadabooks.com/conversations/1969/jun?d=1',
    'https://prabhupadabooks.com/conversations/1969/aug?d=1',
    'https://prabhupadabooks.com/conversations/1969/dec?d=1',
    'https://prabhupadabooks.com/conversations/1970/nov?d=1',
    'https://prabhupadabooks.com/conversations/1970/dec?d=1',
    'https://prabhupadabooks.com/conversations/1971/jan?d=1',
    'https://prabhupadabooks.com/conversations/1971/feb?d=1',
    'https://prabhupadabooks.com/conversations/1971/mar?d=1',
    'https://prabhupadabooks.com/conversations/1971/apr?d=1',
    'https://prabhupadabooks.com/conversations/1971/jun?d=1',
    'https://prabhupadabooks.com/conversations/1971/jul?d=1',
    'https://prabhupadabooks.com/conversations/1971/aug?d=1',
    'https://prabhupadabooks.com/conversations/1971/sep?d=1',
    'https://prabhupadabooks.com/conversations/1971/nov?d=1',
    'https://prabhupadabooks.com/conversations/1972/jan?d=1',
    'https://prabhupadabooks.com/conversations/1972/feb?d=1',
    'https://prabhupadabooks.com/conversations/1972/mar?d=1',
    'https://prabhupadabooks.com/conversations/1972/apr?d=1',
    'https://prabhupadabooks.com/conversations/1972/may?d=1',
    'https://prabhupadabooks.com/conversations/1972/jun?d=1',
    'https://prabhupadabooks.com/conversations/1972/jul?d=1',
    'https://prabhupadabooks.com/conversations/1972/sep?d=1',
    'https://prabhupadabooks.com/conversations/1972/oct?d=1',
    'https://prabhupadabooks.com/conversations/1973/feb?d=1',
    'https://prabhupadabooks.com/conversations/1973/mar?d=1',
    'https://prabhupadabooks.com/conversations/1973/apr?d=1',
    'https://prabhupadabooks.com/conversations/1973/may?d=1',
    'https://prabhupadabooks.com/conversations/1973/jun?d=1',
    'https://prabhupadabooks.com/conversations/1973/jul?d=1',
    'https://prabhupadabooks.com/conversations/1973/aug?d=1',
    'https://prabhupadabooks.com/conversations/1973/sep?d=1',
    'https://prabhupadabooks.com/conversations/1973/nov?d=1',
    'https://prabhupadabooks.com/conversations/1973/dec?d=1',
    'https://prabhupadabooks.com/conversations/1974/jan?d=1',
    'https://prabhupadabooks.com/conversations/1974/feb?d=1',
    'https://prabhupadabooks.com/conversations/1974/mar?d=1',
    'https://prabhupadabooks.com/conversations/1974/apr?d=1',
    'https://prabhupadabooks.com/conversations/1974/may?d=1',
    'https://prabhupadabooks.com/conversations/1974/jun?d=1',
    'https://prabhupadabooks.com/conversations/1974/jul?d=1',
    'https://prabhupadabooks.com/conversations/1974/aug?d=1',
    'https://prabhupadabooks.com/conversations/1974/sep?d=1',
    'https://prabhupadabooks.com/conversations/1975/jan?d=1',
    'https://prabhupadabooks.com/conversations/1975/feb?d=1',
    'https://prabhupadabooks.com/conversations/1975/mar?d=1',
    'https://prabhupadabooks.com/conversations/1975/apr?d=1',
    'https://prabhupadabooks.com/conversations/1975/may?d=1',
    'https://prabhupadabooks.com/conversations/1975/jun?d=1',
    'https://prabhupadabooks.com/conversations/1975/jul?d=1',
    'https://prabhupadabooks.com/conversations/1975/aug?d=1',
    'https://prabhupadabooks.com/conversations/1975/sep?d=1',
    'https://prabhupadabooks.com/conversations/1975/oct?d=1',
    'https://prabhupadabooks.com/conversations/1975/nov?d=1',
    'https://prabhupadabooks.com/conversations/1975/dec?d=1',
    'https://prabhupadabooks.com/conversations/1976/jan?d=1',
    'https://prabhupadabooks.com/conversations/1976/feb?d=1',
    'https://prabhupadabooks.com/conversations/1976/mar?d=1',
    'https://prabhupadabooks.com/conversations/1976/apr?d=1',
    'https://prabhupadabooks.com/conversations/1976/may?d=1',
    'https://prabhupadabooks.com/conversations/1976/jun?d=1',
    'https://prabhupadabooks.com/conversations/1976/jul?d=1'
    ]


# # Headers to include in the request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9'
# }

# # Initialize lists to store the questions and answers
# all_questions = []
# all_answers = []

# # Function to clean the 'answer' text
# def clean_answer(text):
#     return text.replace('Prabhupāda:', '').strip()

# # Loop through each URL and extract conversations
# for url in urls:
#     # Send a GET request to the URL
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()

#     # Parse the HTML content of the webpage
#     soup = BeautifulSoup(response.text, 'html.parser')

#     # Extract the conversation
#     conversation_divs = soup.find_all('div', class_='Purp-para')

#     current_question = None
#     current_answer = ""

#     for div in conversation_divs:
#         bold_tag = div.find('span', class_='Bold')
#         if bold_tag:
#             speaker_tag = bold_tag.find('a')
#             speaker = speaker_tag.get_text(strip=True) if speaker_tag else bold_tag.get_text(strip=True)
#             text = div.get_text(strip=True).replace(f"{speaker}:", "").strip()
            
#             if speaker == "Prabhupāda:":
#                 if current_question:
#                     current_answer += " " + text
#                 else:
#                     current_answer = text
#             else:
#                 if current_question and current_answer:
#                     all_questions.append(current_question)
#                     all_answers.append(clean_answer(current_answer.strip()))
#                 current_question = text
#                 current_answer = ""

#     if current_question and current_answer:
#         all_questions.append(current_question)
#         all_answers.append(clean_answer(current_answer.strip()))

# # Create a DataFrame from the extracted data
# df = pd.DataFrame({
#     'question': all_questions,
#     'answer': all_answers
# })

# # Save the DataFrame to a CSV file
# df.to_csv('all_conversations.csv', index=False, encoding='utf-8')

# print("Data saved to 'all_conversations.csv'")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Headers to include in the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

# Initialize lists to store the questions and answers
questions = []
answers = []

def clean_text(text):
    return ' '.join(text.split()).strip()

# Loop through all URLs and extract conversations
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the conversation
    conversation_divs = soup.find_all('div', class_='Purp-para')

    current_question = None
    current_answer = ""

    for div in conversation_divs:
        bold_tag = div.find('span', class_='Bold')
        if bold_tag:
            speaker_tag = bold_tag.find('a')
            speaker = speaker_tag.get_text(strip=True) if speaker_tag else bold_tag.get_text(strip=True)
            text = div.get_text(strip=True).replace(f"{speaker}:", "").strip()

            if speaker == "Prabhupāda:":
                if current_question:
                    current_answer += " " + text
                else:
                    current_answer = text
            else:
                if current_question and current_answer:
                    questions.append(current_question)
                    answers.append(clean_text(current_answer))
                current_question = text
                current_answer = ""
        else:
            current_answer += " " + div.get_text(strip=True)

    if current_question and current_answer:
        questions.append(current_question)
        answers.append(clean_text(current_answer))

# Create a DataFrame from the extracted data
df = pd.DataFrame({
    'question': questions,
    'answer': answers
})

# Clean up any remaining Prabhupāda references in answers
df['answer'] = df['answer'].apply(lambda x: x.replace('Prabhupāda:', '').strip() if isinstance(x, str) else x)

# Save the DataFrame to a CSV file
df.to_csv('conversation_combined.csv', index=False, encoding='utf-8')

print("Data saved to 'conversation_combined.csv'")

