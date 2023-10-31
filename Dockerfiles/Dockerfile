# Use a lightweight base image
FROM python:3.9-slim

# Install cron
RUN apt-get update && apt-get install -y cron

# Set the working directory
WORKDIR /app

# Copy your Python script to the container
COPY open_website.py .

# Install the required libraries
RUN pip install requests

# Add a cron job schedule
RUN echo "*/5 0-2,7-23 * * * /usr/local/bin/python /app/open_website.py >> /var/log/cron.log 2>&1" | crontab -

# Start the cron service
CMD ["cron", "-f"]

