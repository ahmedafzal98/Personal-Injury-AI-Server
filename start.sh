#!/bin/bash
# Install Tesseract
apt-get update
apt-get install -y tesseract-ocr

# Start FastAPI
uvicorn main:app --host 0.0.0.0 --port $PORT
