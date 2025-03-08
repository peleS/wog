FROM python:3.9

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget unzip curl xvfb libxi6 libgconf-2-4 \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

# install Chrome
RUN wget -qO- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor > /usr/share/keyrings/google-chrome.gpg
RUN echo 'deb [signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main' \
    | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

ENV CHROME_DRIVER_VERSION=119.0.6045.105
RUN wget -q "https://chromedriver.storage.googleapis.com/${CHROME_DRIVER_VERSION}/chromedriver_linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver
COPY app.py .
COPY Scores.txt ./Scores.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application port
EXPOSE 8777
CMD ["python", "main_score.py"]
