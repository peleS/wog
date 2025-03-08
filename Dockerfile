FROM python:3.9

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl xvfb libxi6 libgconf-2-4 \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -qO- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome.gpg
RUN echo 'deb [signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' \
    | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d. -f1) && \
    wget -q "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_${CHROME_VERSION}" -O /tmp/chrome_driver_version && \
    CHROME_DRIVER_VERSION=$(cat /tmp/chrome_driver_version) && \
    wget -q "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_DRIVER_VERSION}/linux64/chromedriver-linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver-linux64 /tmp/chromedriver.zip /tmp/chrome_driver_version

# Copy all project files
COPY . .

# Ensure Scores.txt is included
COPY Scores.txt /Scores.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8777
CMD ["python", "main_score.py"]