# Use a Debian-based image
FROM debian:latest

# Install Python and the python3-psutil package
RUN apt-get update && apt-get install -y python3 python3-psutil

# Set the working directory
WORKDIR /app

# Copy scripts from host to the container working directory
COPY scripts/ ./

# Run the script
CMD ["python3", "SystemHealth.py"]
