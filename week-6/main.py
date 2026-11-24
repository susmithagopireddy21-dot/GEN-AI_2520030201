import json
import csv
import requests
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

INPUT_FILE = "golden_set.json"
OUTPUT_FILE = "baseline_results.csv"


def load_questions():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_llm_answer(question):
    payload = {
        "model": MODEL_NAME,
        "prompt": question,
        "stream": False,
        "options": {
            "temperature": 0
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()
    return response.json()["response"].strip()


def calculate_score(answer, expected_keywords):
    answer = answer.lower()

    matched = []
    missing = []

    for keyword in expected_keywords:
        if keyword.lower() in answer:
            matched.append(keyword)
        else:
            missing.append(keyword)

    if len(expected_keywords) > 0:
        score = (len(matched) / len(expected_keywords)) * 100
    else:
        score = 0

    return round(score, 2), matched, missing
questions = load_questions()
results = []

for item in questions:
    question_id = item["id"]
    question = item["question"]
    expected_answer = item["expected_answer"]
    expected_keywords = item["keywords"]
    source = item["source"]

    print("\nEvaluating:", question_id)

    try:
        llm_answer = get_llm_answer(question)

        score, matched, missing = calculate_score(
            llm_answer,
            expected_keywords
        )

        status = "PASS" if score >= 60 else "REVIEW"

        print("Score:", score)
        print("Status:", status)

    except Exception as error:
        llm_answer = str(error)
        matched = []
        missing = []
        score = 0
        status = "ERROR"

        print("Error:", error)

    results.append({
        "Question_ID": question_id,
        "Question": question,
        "Expected_Answer": expected_answer,
        "LLM_Answer": llm_answer,
        "Matched_Keywords": ", ".join(matched),
        "Missing_Keywords": ", ".join(missing),
        "Score": score,
        "Status": status,
        "Source": source,
        "Model": MODEL_NAME,
        "Release": "v0.1"
    })
    fieldnames = [
    "Question_ID",
    "Question",
    "Expected_Answer",
    "LLM_Answer",
    "Matched_Keywords",
    "Missing_Keywords",
    "Score",
    "Status",
    "Source",
    "Model",
    "Release"
]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("\nCSV file created successfully:", OUTPUT_FILE)
successful = [r for r in results if r["Status"] != "ERROR"]

passed = sum(1 for r in results if r["Status"] == "PASS")
review = sum(1 for r in results if r["Status"] == "REVIEW")
errors = sum(1 for r in results if r["Status"] == "ERROR")

if successful:
    average_score = sum(r["Score"] for r in successful) / len(successful)
else:
    average_score = 0

print("\n========== EVALUATION SUMMARY ==========")
print("Release:", "v0.1")
print("Model:", MODEL_NAME)
print("Total Questions:", len(results))
print("Successful Responses:", len(successful))
print("Passed:", passed)
print("Review:", review)
print("Errors:", errors)
print("Average Keyword Coverage:", round(average_score, 2), "%")
print("Evaluation Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Results Saved:", OUTPUT_FILE)
print("Evaluation Completed!")