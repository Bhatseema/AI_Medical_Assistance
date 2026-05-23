import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_MODEL = "llama3-8b-8192"

DATA_PATH = "data"
DB_PATH = "db/faiss_index"