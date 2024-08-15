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
# urls = [
#     'https://prabhupadabooks.com/conversations/1967/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1968/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1968/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1969/jan?d=1',
#     'https://prabhupadabooks.com/conversations/1969/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1969/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1969/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1969/may?d=1',
#     'https://prabhupadabooks.com/conversations/1969/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1969/aug?d=1',
#     'https://prabhupadabooks.com/conversations/1969/dec?d=1',
#     'https://prabhupadabooks.com/conversations/1970/nov?d=1',
#     'https://prabhupadabooks.com/conversations/1970/dec?d=1',
#     'https://prabhupadabooks.com/conversations/1971/jan?d=1',
#     'https://prabhupadabooks.com/conversations/1971/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1971/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1971/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1971/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1971/jul?d=1',
#     'https://prabhupadabooks.com/conversations/1971/aug?d=1',
#     'https://prabhupadabooks.com/conversations/1971/sep?d=1',
#     'https://prabhupadabooks.com/conversations/1971/nov?d=1',
#     'https://prabhupadabooks.com/conversations/1972/jan?d=1',
#     'https://prabhupadabooks.com/conversations/1972/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1972/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1972/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1972/may?d=1',
#     'https://prabhupadabooks.com/conversations/1972/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1972/jul?d=1',
#     'https://prabhupadabooks.com/conversations/1972/sep?d=1',
#     'https://prabhupadabooks.com/conversations/1972/oct?d=1',
#     'https://prabhupadabooks.com/conversations/1973/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1973/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1973/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1973/may?d=1',
#     'https://prabhupadabooks.com/conversations/1973/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1973/jul?d=1',
#     'https://prabhupadabooks.com/conversations/1973/aug?d=1',
#     'https://prabhupadabooks.com/conversations/1973/sep?d=1',
#     'https://prabhupadabooks.com/conversations/1973/nov?d=1',
#     'https://prabhupadabooks.com/conversations/1973/dec?d=1',
#     'https://prabhupadabooks.com/conversations/1974/jan?d=1',
#     'https://prabhupadabooks.com/conversations/1974/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1974/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1974/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1974/may?d=1',
#     'https://prabhupadabooks.com/conversations/1974/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1974/jul?d=1',
#     'https://prabhupadabooks.com/conversations/1974/aug?d=1',
#     'https://prabhupadabooks.com/conversations/1974/sep?d=1',
#     'https://prabhupadabooks.com/conversations/1975/jan?d=1',
#     'https://prabhupadabooks.com/conversations/1975/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1975/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1975/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1975/may?d=1',
#     'https://prabhupadabooks.com/conversations/1975/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1975/jul?d=1',
#     'https://prabhupadabooks.com/conversations/1975/aug?d=1',
#     'https://prabhupadabooks.com/conversations/1975/sep?d=1',
#     'https://prabhupadabooks.com/conversations/1975/oct?d=1',
#     'https://prabhupadabooks.com/conversations/1975/nov?d=1',
#     'https://prabhupadabooks.com/conversations/1975/dec?d=1',
#     'https://prabhupadabooks.com/conversations/1976/jan?d=1',
#     'https://prabhupadabooks.com/conversations/1976/feb?d=1',
#     'https://prabhupadabooks.com/conversations/1976/mar?d=1',
#     'https://prabhupadabooks.com/conversations/1976/apr?d=1',
#     'https://prabhupadabooks.com/conversations/1976/may?d=1',
#     'https://prabhupadabooks.com/conversations/1976/jun?d=1',
#     'https://prabhupadabooks.com/conversations/1976/jul?d=1'
#     ]


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

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Headers to include in the request
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9'
# }

# # Initialize lists to store the questions and answers
# questions = []
# answers = []

# def clean_text(text):
#     return ' '.join(text.split()).strip()

# # Loop through all URLs and extract conversations
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
#                     questions.append(current_question)
#                     answers.append(clean_text(current_answer))
#                 current_question = text
#                 current_answer = ""
#         else:
#             current_answer += " " + div.get_text(strip=True)

#     if current_question and current_answer:
#         questions.append(current_question)
#         answers.append(clean_text(current_answer))

# # Create a DataFrame from the extracted data
# df = pd.DataFrame({
#     'question': questions,
#     'answer': answers
# })

# # Clean up any remaining Prabhupāda references in answers
# df['answer'] = df['answer'].apply(lambda x: x.replace('Prabhupāda:', '').strip() if isinstance(x, str) else x)

# # Save the DataFrame to a CSV file
# df.to_csv('conversation_combined.csv', index=False, encoding='utf-8')

# print("Data saved to 'conversation_combined.csv'")

##################################################################################################

# import requests
# from bs4 import BeautifulSoup
# import json

# # Define the URLs of the three parts of the book
# urls = {
#     "Adi": "https://vedabase.io/en/library/cc/adi/",
#     "Madhya": "https://vedabase.io/en/library/cc/madhya/",
#     "Antya": "https://vedabase.io/en/library/cc/antya/"
# }

# # Define the number of chapters in each part
# chapters = {
#     "Adi": 17,
#     "Madhya": 25,
#     "Antya": 20
# }

# # Initialize a dictionary to store the data
# data = {}

# # Function to scrape a single chapter
# def scrape_chapter(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     chapter_data = {
#         "Paragraph": [],
#         "Texts": {}
#     }

#     content_div = soup.find('div', id='content')

#     # Get chapter name
#     chapter_name = content_div.find('div', class_='r-chapter-title').get_text(strip=True)
    
#     # Get all paragraphs
#     paragraphs = content_div.find_all('div', class_='r-paragraph')
#     for p in paragraphs:
#         chapter_data["Paragraph"].append(p.get_text(strip=True))

#     # Get all texts
#     verses = content_div.find_all('dl', class_='r-verse')
#     for verse in verses:
#         text_id = verse.find('dt').get_text(strip=True)
#         text_content = verse.find('dd').get_text(strip=True)
#         chapter_data["Texts"][text_id] = text_content

#     return chapter_name, chapter_data

# # Iterate over each part of the book
# for part, base_url in urls.items():
#     data[part] = {}

#     # Iterate over each chapter
#     for chapter_num in range(1, chapters[part] + 1):
#         chapter_url = f"{base_url}{chapter_num}/"
#         chapter_name, chapter_data = scrape_chapter(chapter_url)
#         data[part][f"Chapter {chapter_num}"] = {
#             "Chapter Name": chapter_name,
#             "Content": chapter_data
#         }
#         print(f"Scraped {part} Chapter {chapter_num}")

# # Save the data to a JSON file
# with open('sri_caitanya_caritamrta_data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

############################################################################################################

# import requests
# from bs4 import BeautifulSoup
# import json

# # Function to extract data from a given chapter URL
# def extract_chapter_data(chapter_url):
#     response = requests.get(chapter_url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     chapter_data = {}
    
#     # Extract chapter number and title
#     chapter_number = soup.find('div', class_='r-title-small').h1.text.strip()
#     chapter_title = soup.find('div', class_='r-chapter-title').h1.text.strip()
    
#     # Extract paragraphs
#     paragraphs = [p.text.strip() for p in soup.find_all('div', class_='r-paragraph')]
    
#     chapter_data['chapter_number'] = chapter_number
#     chapter_data['chapter_title'] = chapter_title
#     chapter_data['content'] = paragraphs
    
#     return chapter_data

# # Base URL for the chapters
# base_url = "https://vedabase.io/en/library/kb/"
# num_chapters = 90

# # Dictionary to hold the entire book data
# book_data = {}

# # Iterate through all chapters and extract data
# for chapter in range(1, num_chapters + 1):
#     chapter_url = f"{base_url}{chapter}/"
#     print(f"Extracting data from: {chapter_url}")
#     chapter_data = extract_chapter_data(chapter_url)
#     book_data[chapter] = chapter_data

# # Save the data to a JSON file
# with open('krishna_supreme_personality.json', 'w', encoding='utf-8') as json_file:
#     json.dump(book_data, json_file, ensure_ascii=False, indent=4)

# print("Data extraction complete and saved to krishna_supreme_personality.json")

############################################################################################

# import requests
# from bs4 import BeautifulSoup
# import json

# # Function to extract data from a given chapter URL
# def extract_chapter_data(chapter_url):
#     response = requests.get(chapter_url)
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     chapter_data = {}
    
#     # Extract chapter number and title
#     chapter_number = soup.find('div', class_='r-title-small').h1.text.strip()
#     chapter_title = soup.find('div', class_='r-chapter-title').h1.text.strip()
    
#     # Extract paragraphs
#     paragraphs = [p.text.strip() for p in soup.find_all('div', class_='r-paragraph')]
#     verses = [p.text.strip() for p in soup.find_all('div', class_='r-verse-text')]
    
#     chapter_data['chapter_number'] = chapter_number
#     chapter_data['chapter_title'] = chapter_title
#     chapter_data['content'] = paragraphs + verses
    
#     return chapter_data

# # Base URL for the chapters
# base_url = "https://vedabase.io/en/library/tlc/"
# num_chapters = 32

# # Dictionary to hold the entire book data
# book_data = {}

# # Iterate through all chapters and extract data
# for chapter in range(1, num_chapters + 1):
#     chapter_url = f"{base_url}{chapter}/"
#     print(f"Extracting data from: {chapter_url}")
#     chapter_data = extract_chapter_data(chapter_url)
#     book_data[chapter] = chapter_data

# # Save the data to a JSON file
# with open('teachings_of_lord_caitanya.json', 'w', encoding='utf-8') as json_file:
#     json.dump(book_data, json_file, ensure_ascii=False, indent=4)

# print("Data extraction complete and saved to teachings_of_lord_caitanya.json")

############################################################################################

# import requests
# from bs4 import BeautifulSoup
# import json

# BASE_URL = "https://vedabase.io/en/library/noi"
# NUM_TEXTS = 11  # Number of texts in Nectar of Instruction

# def fetch_page(url):
#     response = requests.get(url)
#     if response.status_code == 404 or "Page not found" in response.text:
#         return None
#     return response.text

# def parse_text_page(soup):
#     text_data = {}

#     # Extract Devanagari (if available)
#     devanagari_section = soup.find("div", class_="wrapper-devanagari")
#     if devanagari_section:
#         text_data["Devanagari"] = devanagari_section.get_text(strip=True)

#     # Extract Text
#     text_section = soup.find("div", class_="wrapper-verse-text")
#     if text_section:
#         text_data["Text"] = text_section.get_text(strip=True)

#     # Extract Synonyms
#     synonyms_section = soup.find("div", class_="wrapper-synonyms")
#     if synonyms_section:
#         text_data["Synonyms"] = synonyms_section.get_text(strip=True)

#     # Extract Translation
#     translation_section = soup.find("div", class_="wrapper-translation")
#     if translation_section:
#         text_data["Translation"] = translation_section.get_text(strip=True)

#     # Extract Purport
#     purport_section = soup.find("div", class_="wrapper-purport")
#     if purport_section:
#         purport_text = ""
#         for paragraph in purport_section.find_all("div", class_="r-lang-en r-paragraph"):
#             purport_text += paragraph.get_text(strip=True) + "\n"
#         text_data["Purport"] = purport_text.strip()

#     return text_data

# def scrape_text(text_number):
#     text_data = {}

#     text_url = f"{BASE_URL}/{text_number}/"
#     print(f"Scraping Text URL: {text_url}")
#     text_page = fetch_page(text_url)
    
#     if not text_page:
#         return None

#     text_soup = BeautifulSoup(text_page, "html.parser")
#     text_data = parse_text_page(text_soup)
    
#     return text_data

# def main():
#     nectar_of_instruction_data = {}

#     for text_number in range(1, NUM_TEXTS + 1):
#         print(f"Scraping Text {text_number}")
#         text_data = scrape_text(text_number)
#         if text_data:
#             nectar_of_instruction_data[f"Text {text_number}"] = text_data

#     # Write data to JSON
#     with open("nectar_of_instruction_data.json", "w", encoding="utf-8") as f:
#         json.dump(nectar_of_instruction_data, f, ensure_ascii=False, indent=4)

# if __name__ == "__main__":
#     main()

############################################################################################

# import requests
# from bs4 import BeautifulSoup
# import json

# BASE_URL = "https://vedabase.io/en/library/tlk"
# NUM_TEXTS = 18  # Number of texts in the Teachings of Lord Kapila

# def fetch_page(url):
#     response = requests.get(url)
#     if response.status_code == 404 or "Page not found" in response.text:
#         return None
#     return response.text

# def parse_text_page(soup):
#     text_data = {}

#     # Extract Chapter Number
#     chapter_number = soup.find("div", class_="r-title-small r-chapter")
#     if chapter_number:
#         text_data["Chapter"] = chapter_number.get_text(strip=True)

#     # Extract Chapter Title
#     chapter_title = soup.find("div", class_="r-chapter-title r-title")
#     if chapter_title:
#         text_data["Title"] = chapter_title.get_text(strip=True)

#     # Extract Text Number
#     text_number = soup.find("div", class_="r-small-header")
#     if text_number:
#         text_data["Text Number"] = text_number.get_text(strip=True)

#     # Extract Verse Text
#     verse_text = soup.find("div", class_="r-verse-text")
#     if verse_text:
#         text_data["Verse"] = verse_text.get_text(strip=True)

#     # Extract Translation
#     translation_section = soup.find("div", class_="r-translation")
#     if translation_section:
#         text_data["Translation"] = translation_section.get_text(strip=True)

#     # Extract Paragraphs
#     paragraph_section = soup.find_all("div", class_="r-paragraph")
#     paragraphs = []
#     for paragraph in paragraph_section:
#         paragraphs.append(paragraph.get_text(strip=True))
#     text_data["Purport"] = "\n".join(paragraphs)

#     return text_data

# def scrape_text(text_number):
#     text_data = {}
#     text_url = f"{BASE_URL}/{text_number}/"
#     print(f"Scraping Text URL: {text_url}")
#     text_page = fetch_page(text_url)
    
#     if not text_page:
#         return None

#     text_soup = BeautifulSoup(text_page, "html.parser")
#     text_data = parse_text_page(text_soup)

#     return text_data

# def main():
#     teachings_of_lord_kapila_data = {}

#     for text_number in range(1, NUM_TEXTS + 1):
#         print(f"Scraping Text {text_number}")
#         text_data = scrape_text(text_number)
#         if text_data:
#             teachings_of_lord_kapila_data[f"Text {text_number}"] = text_data

#     # Write data to JSON
#     with open("teachings_of_lord_kapila.json", "w", encoding="utf-8") as f:
#         json.dump(teachings_of_lord_kapila_data, f, ensure_ascii=False, indent=4)

# if __name__ == "__main__":
#     main()

############################################################################################

