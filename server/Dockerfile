# Use Python slim image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port for Render
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
