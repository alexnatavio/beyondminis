# Use a Debian-based image
FROM debian:latest

# Install Python and the python3-psutil package
RUN apt-get update && apt-get install -y python3 python3-psutil

# Set the working directory
WORKDIR /app

# Copy your Python scripts from the host to the container's working directory
COPY scripts/ ./

# Run your Python script
CMD ["python3", "SystemHealth.py"]
