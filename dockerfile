# Use the selenium standalone chrome image as the base
FROM selenium/standalone-chrome

# Switch to root to install Python and other dependencies
USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set python3 as the default python version
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copy the Python script into the container
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir selenium webdriver_manager requests

# Run the script with Python when the container launches
CMD ["python", "headlesstest.py"]
