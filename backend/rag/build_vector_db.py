import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from rag.embeddings import embedding_model

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

KB_PATH = os.path.join(BASE_DIR, "knowledge_base")
VECTOR_PATH = os.path.join(BASE_DIR, "rag", "vectorstores")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

os.makedirs(VECTOR_PATH, exist_ok=True)

for category in os.listdir(KB_PATH):

    category_path = os.path.join(KB_PATH, category)

    if not os.path.isdir(category_path):
        continue

    docs = []

    print(f"\nProcessing {category}")

    for file in os.listdir(category_path):

        if file.endswith(".pdf"):

            pdf = os.path.join(category_path, file)

            loader = PyPDFLoader(pdf)

            docs.extend(loader.load())

    if len(docs) == 0:
        print("No PDFs Found")
        continue

    chunks = splitter.split_documents(docs)

    print(f"Chunks Created : {len(chunks)}")

    db = FAISS.from_documents(
        chunks,
        embedding_model
    )

    save_dir = os.path.join(
        VECTOR_PATH,
        category
    )

    db.save_local(save_dir)

    print("Vector Database Saved")