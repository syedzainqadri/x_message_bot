# # Use the official Python base image
# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file into the container
# COPY requirements.txt .

# # Install any dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Install GnuPG and necessary tools
# RUN apt-get update && apt-get install -y gnupg wget unzip curl

# # Download the Google Chrome signing key and add it to the keyring
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-archive-keyring.gpg || echo "Failed to download and decode the signing key"

# # Add the Google Chrome repository URL to the sources list
# RUN echo "deb [signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list || echo "Failed to add repository URL"

# # Update package lists and install Google Chrome Stable
# RUN apt-get update && apt-get install -y google-chrome-stable --no-install-recommends || echo "Failed to install Google Chrome Stable"

# # Install Selenium
# RUN pip install selenium

# # Download and install ChromeDriver
# RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
#     wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
#     unzip /tmp/chromedriver.zip -d /usr/local/bin && \
#     rm /tmp/chromedriver.zip

# Use a Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install wget and gnupg, then add Google Chrome repository
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget \
        gnupg \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' > /etc/apt/sources.list.d/google-chrome.list

# Install Google Chrome and necessary dependencies for Selenium
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install required Python packages
RUN pip install --upgrade pip \
    && pip install selenium requests webdriver_manager

# Set the working directory in the container
WORKDIR /app

# Copy the script and any other necessary files into the container
COPY . /app

# Copy the Python script into the container
COPY XPosting.py .

# Run the Python script when the container launches
CMD ["python", "XPosting.py"]
