from fastapi import APIRouter, UploadFile, File, HTTPException, Query
import shutil
import os
import uuid

from app.document_loader import load_pdf
from app.vector_store import create_vector_store
from app.rag_pipeline import get_answer

router = APIRouter()

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)


# -----------------------------
# 📄 UPLOAD ENDPOINT
# -----------------------------
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file uploaded")

        file_path = os.path.join(DATA_PATH, f"{uuid.uuid4()}.pdf")

        file.file.seek(0)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # process PDF
        docs = load_pdf(file_path)
        create_vector_store(docs)

        return {
            "message": "File uploaded and indexed successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# 💬 ASK ENDPOINT (MISSING BEFORE - FIXED NOW)
# -----------------------------
@router.post("/ask")
async def ask_question(query: str = Query(...)):
    try:
        answer, docs = get_answer(query)

        return {
            "answer": answer,
            "sources": [doc.metadata for doc in docs]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))