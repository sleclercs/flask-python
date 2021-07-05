# Using official python runtime base image
FROM python:3

WORKDIR /usr/src/app

# Install our requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy our code from the current folder to /app inside the container
ADD . ./

# Make port 5000 available for links and/or publish
EXPOSE 5000

# Define our command to be run when launching the container
#CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
CMD ["python", "./app.py"]




