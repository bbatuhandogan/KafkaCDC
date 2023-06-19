# Use a Docker image based on Python 3.8.10
FROM python:3.8.10

# Set /app as the working directory
WORKDIR /app

# Copy files from the current directory to /app directory
ADD . /app

# Install dependencies listed in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run consumer.py when the Docker container starts
CMD ["python", "consumer.py"]
