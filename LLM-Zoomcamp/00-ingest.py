# In the notebook.ipynb, we built the RAG flow piece by piece - search, then the prompt, then the LLM call. The pipeline works, but every time we want to use it, we need to repeat the same code.

# Ingest.py - Loading data and building the search index

import requests
from minsearch import Index

# Load the FAQ data from the DataTalksClub website
def load_faq_data():
    docs_url = "https://datatalks.club/faq/json/courses.json"
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents = []
    url_prefix = "https://datatalks.club/faq"

    for course in courses_raw:
        course_url = f"""{url_prefix}/{course['path']}"""
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents


# Build the search index using MinSearch
def build_index(documents):
    index = Index(
        text_fields=["question", "section", "answer"],
        keyword_fields=["course"]
    )
    index.fit(documents)
    return index