FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && edot-bootstrap --action=install  # Auto-installs supported instrumentations

# Copy application code
COPY app.py .

# Expose FastAPI port
EXPOSE 8000

# Run with OpenTelemetry instrumentation
CMD ["opentelemetry-instrument", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
