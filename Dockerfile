# Use Python Alpine base image with a specific version
FROM python:3.9-alpine3.14

# Update apk package manager
RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash

# Add a user group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Set the working directory
WORKDIR /app

# Copy requirements.txt first to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the container user
USER appuser

# Expose the port on which the application will run
EXPOSE 8081

# Set the default command to run the application
CMD ["python3", "main.py"]
