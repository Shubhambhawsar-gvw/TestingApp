FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Compile Python files to .pyc and remove .py
RUN python -m compileall . \
    && find . -name "*.py" -type f -delete

# Expose the Flask port
EXPOSE 5700

# Run the compiled app
CMD ["python", "__pycache__/app.cpython-311.pyc"]
