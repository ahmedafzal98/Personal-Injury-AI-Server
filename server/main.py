from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from extractor import extract_text_auto
import shutil
import os

app = FastAPI(title="Document Extraction API", version="1.0")

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- for development, allow all origins (React frontend)
    allow_credentials=True,
    allow_methods=["*"],  # <-- allow all HTTP methods: GET, POST, etc.
    allow_headers=["*"],  # <-- allow all headers
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def root():
    return {"message": "Welcome to Ahmed's Document Extraction API 🚀"}

@app.post("/extract")
async def extract_text(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file temporarily
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Call your extractor function
        text = extract_text_auto(file_path)

        # Delete file after processing (optional)
        os.remove(file_path)

        return {
            "filename": file.filename,
            "text_length": len(text),
            "extracted_text": text,
        }
    except Exception as e:
        return {"error": str(e)}
