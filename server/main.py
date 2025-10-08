from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from extractor import extract_text_auto
import shutil
import os

app = FastAPI(title="Document Extraction API", version="1.0")

# ✅ CORS FIX HERE
origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://personal-injury-ai-client.onrender.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Welcome to Ahmed's Document Extraction API 🚀"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        text = extract_text_auto(file_path)
        os.remove(file_path)
        return {
            "filename": file.filename,
            "text_length": len(text),
            "extracted_text": text,
        }
    except Exception as e:
        return {"error": str(e)}
