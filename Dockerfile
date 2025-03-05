# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose port 8080 (required by Cloud Run)
EXPOSE 8080

# Run the application using Uvicorn, listening on the PORT environment variable or default to 8080
CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "$PORT"]