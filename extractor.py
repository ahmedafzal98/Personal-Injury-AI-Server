import mimetypes
import os
from PIL import Image
import pytesseract
import pdfplumber
from pdf2image import convert_from_path
import docx2txt

# -------------------------------
# 🔍 Detect File Type
# -------------------------------
def detect_file_type(file_path):
    file_type, _ = mimetypes.guess_type(file_path)
    if not file_type:
        return "unknown"
    elif "image" in file_type:
        return "image"
    elif "pdf" in file_type:
        return "pdf"
    elif "word" in file_type or file_path.endswith(".docx"):
        return "docx"
    elif "text" in file_type:
        return "text"
    else:
        return "unknown"

# -------------------------------
# 🧠 Smart PDF Extraction
# -------------------------------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text += page_text

    # 🧠 Smart detection: scanned vs text-based PDF
    if not text.strip():
        print("⚠️ No text found — scanned PDF detected, switching to OCR...")
        pages = convert_from_path(file_path)
        for page_number, page in enumerate(pages, start=1):
            print(f"🔍 OCR processing page {page_number}...")
            text += pytesseract.image_to_string(page)
    else:
        print("✅ Text-based PDF detected.")

    return text

# -------------------------------
# 🖼️ Image Extraction
# -------------------------------
def extract_text_from_image(file_path):
    img = Image.open(file_path)
    return pytesseract.image_to_string(img)

# -------------------------------
# 📝 DOCX Extraction
# -------------------------------
def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)

# -------------------------------
# 📜 TXT Extraction
# -------------------------------
def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# -------------------------------
# 🚀 Main Function (Auto Extract)
# -------------------------------
def extract_text_auto(file_path):
    file_type = detect_file_type(file_path)
    print(f"📁 Detected file type: {file_type}")

    if file_type == "image":
        return extract_text_from_image(file_path)

    elif file_type == "pdf":
        return extract_text_from_pdf(file_path)

    elif file_type == "docx":
        return extract_text_from_docx(file_path)

    elif file_type == "text":
        return extract_text_from_txt(file_path)

    else:
        return "❌ Unsupported or unknown file type."


# -------------------------------
# 🧪 Example Usage
# -------------------------------
if __name__ == "__main__":
    test_files = [
        "AhmedAfzalResume.pdf",
        "img1.jpeg",
    ]

    for file in test_files:
        if os.path.exists(file):
            print("\n-----------------------------")
            print(f"🔹 Extracting from: {file}")
            print("-----------------------------")
            text = extract_text_auto(file)
            print(text[:1000])  # print first 1000 chars
        else:
            print(f"⚠️ File not found: {file}")
