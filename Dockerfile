# Use Python Alpine
FROM python:3.10-alpine

# Install Git
RUN apk add --no-cache git github-cli

# Create a working directory
WORKDIR /app

# Copy the requirements.txt to the current directory
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy our mirror script
COPY mirror.py /app/mirror.py

# Make an output directory
RUN mkdir /app/output


# Create a volume for the output directory
VOLUME ["/app/output"]

# By default, run the mirror script
CMD ["python", "/app/mirror.py"]
