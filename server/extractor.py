import mimetypes
import os
from PIL import Image, ImageEnhance, ImageFilter
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
# 🖼️ Preprocess Images for OCR
# -------------------------------
def preprocess_image(img):
    """Convert image to grayscale, enhance contrast, reduce noise."""
    img = img.convert("L")  # Grayscale
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)  # Increase contrast
    width, height = img.size
    if width < 1000:  # Resize small images
        img = img.resize((width*2, height*2))
    return img

# -------------------------------
# 🖼️ Image Extraction (Improved)
# -------------------------------
def extract_text_from_image(file_path):
    try:
        img = Image.open(file_path)
        img = preprocess_image(img)
        text = pytesseract.image_to_string(img, lang="eng", config="--psm 6 --oem 3")
        return text.strip()
    except Exception as e:
        return f"❌ OCR failed: {str(e)}"

# -------------------------------
# 🧠 PDF Extraction (Text + Scanned)
# -------------------------------
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text += page_text

    # If no text found, treat as scanned PDF → OCR each page
    if not text.strip():
        print("⚠️ No text found — scanned PDF detected, switching to OCR...")
        pages = convert_from_path(file_path)
        for page_number, page in enumerate(pages, start=1):
            print(f"🔍 OCR processing page {page_number}...")
            page = preprocess_image(page)
            text += pytesseract.image_to_string(page, lang="eng", config="--psm 6 --oem 3")
    else:
        print("✅ Text-based PDF detected.")

    return text.strip()

# -------------------------------
# 📝 DOCX Extraction
# -------------------------------
def extract_text_from_docx(file_path):
    return docx2txt.process(file_path).strip()

# -------------------------------
# 📜 TXT Extraction
# -------------------------------
def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()

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
            print(text[:1000])  # Print first 1000 characters
        else:
            print(f"⚠️ File not found: {file}")
