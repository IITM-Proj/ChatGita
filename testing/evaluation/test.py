from langchain_community.llms.ollama import Ollama
import json

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'True' or 'False') Does the actual response match the expected response? 
"""

GEN_PROMPT = """
{question}
"""


def test_pqpa(qna):
    print(query_and_validate(qna))


def gen(prompt: str):
    model = Ollama(model="llama3.1")
    response_text = model.invoke(prompt)
    return response_text

def query_and_validate(qna: list):
    otp = []
    for qna_item in qna:
        question = qna_item["question"]
        expected_response = qna_item["answer"]

        response_text = gen(question)
        prompt = EVAL_PROMPT.format(
            expected_response=expected_response, actual_response=response_text
        )

        model = Ollama(model="llama3.1")
        evaluation_results_str = model.invoke(prompt)
        evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

        # print(prompt)

        if "true" in evaluation_results_str_cleaned:
            # print("\033[92m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
            otp.append(True)
        elif "false" in evaluation_results_str_cleaned:
            # print("\033[91m" + f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
            otp.append(False)
        else:
            # raise ValueError(
            #     f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
            # )
            otp.append("Invalid")

    return otp

# qna = [
#     {
#         "question": "How much total money does a player start with in Monopoly? (Answer with the number only)",
#         "expected_response": "$1500",
#     },
#     {
#         "question": "How much total money does a player start with in Monopoly? (Answer with the number only)",
#         "expected_response": "$1000",
#     },
# ]

qna = json.load(open(r"C:\Users\karti\Unknown\ChatGita\data\books\perfect_questions_perfect_answers\pqpa.json"))

test_pqpa(qna)