# Gunakan image Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Salin semua file ke container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8080

# Jalankan aplikasi
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]