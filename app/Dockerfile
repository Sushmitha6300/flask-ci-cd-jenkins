# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

# Expose port and run
EXPOSE 5000
CMD ["python", "app.py"]

