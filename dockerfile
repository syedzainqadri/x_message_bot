# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install GnuPG and necessary tools
RUN apt-get update && apt-get install -y gnupg wget unzip curl

# Download the Google Chrome signing key and add it to the keyring
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome-archive-keyring.gpg || echo "Failed to download and decode the signing key"

# Add the Google Chrome repository URL to the sources list
RUN echo "deb [signed-by=/usr/share/keyrings/google-chrome-archive-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list || echo "Failed to add repository URL"

# Update package lists and install Google Chrome Stable
RUN apt-get update && apt-get install -y google-chrome-stable --no-install-recommends || echo "Failed to install Google Chrome Stable"

# Install Selenium
RUN pip install selenium

# Download and install ChromeDriver
RUN CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` && \
    wget -q -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    rm /tmp/chromedriver.zip

# Copy the Python script into the container
COPY XPosting.py .

# Run the Python script when the container launches
CMD ["python", "XPosting.py"]
