# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory to the project root (same as where Dockerfile is)
WORKDIR /LEARNING_PYTHON

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to run tests
CMD ["pytest", "tests/test_script.py"]
