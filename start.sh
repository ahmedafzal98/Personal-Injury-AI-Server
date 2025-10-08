#!/bin/bash
set -e

# Install Tesseract OCR
apt-get update && apt-get install -y tesseract-ocr

# Move into the server directory
cd server

# Run your FastAPI app
exec uvicorn main:app --host 0.0.0.0 --port 10000
