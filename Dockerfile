FROM selenium/standalone-chrome:latest

# Install Python and pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

WORKDIR /app

# Create and activate virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy only application files
COPY . /app/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=main_score.py

# Set correct permissions
RUN chown -R seluser:seluser /app
USER seluser

EXPOSE 8777
CMD sh -c "python3 main_score.py & sleep 8 && python3 test/e2e.py || exit 1"
