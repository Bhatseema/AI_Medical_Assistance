from langchain_community.vectorstores import FAISS
from app.embeddings import HFEmbeddings
from app.config import DB_PATH
import os


def create_vector_store(docs):
    embedding = HFEmbeddings()

    db = FAISS.from_documents(docs, embedding)

    # Ensure folder exists
    os.makedirs(DB_PATH, exist_ok=True)

    db.save_local(DB_PATH)


def load_vector_store():
    embedding = HFEmbeddings()

    # Check if DB exists before loading
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError("Vector DB not found. Upload documents first.")

    return FAISS.load_local(
        DB_PATH,
        embedding,
        allow_dangerous_deserialization=True
    )