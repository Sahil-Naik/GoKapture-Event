# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to prevent Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set environment variables for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
# Change to 'production' in a production environment

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
