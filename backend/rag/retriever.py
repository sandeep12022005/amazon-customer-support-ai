import os
from langchain_community.vectorstores import FAISS
from rag.embeddings import embedding_model

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
VECTOR_PATH = os.path.join(BASE_DIR, "rag", "vectorstores")

VECTOR_DBS = {}

for category in os.listdir(VECTOR_PATH):

    path = os.path.join(VECTOR_PATH, category)

    if os.path.isdir(path):

        VECTOR_DBS[category] = FAISS.load_local(
            path,
            embedding_model,
            allow_dangerous_deserialization=True
        )

print("Loaded:", list(VECTOR_DBS.keys()))


def retrieve_context(question, categories, k=3):

    if isinstance(categories, str):
        categories = [categories]

    all_docs = []

    for category in categories:

        if category not in VECTOR_DBS:
            continue

        docs = VECTOR_DBS[category].similarity_search(question, k=k)

        all_docs.extend(docs)

    context = ""

    for doc in all_docs:

        context += doc.page_content
        context += "\n\n"

    return context