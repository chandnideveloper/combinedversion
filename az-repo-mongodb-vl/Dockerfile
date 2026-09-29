FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose port (default 8008 or Render PORT env)
EXPOSE 8008

# Run Uvicorn server using environment PORT if provided
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8008}"]
