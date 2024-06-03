# Use an official Python runtime as a parent image
FROM apache/airflow:2.8.2

# Copy the current directory contents into the container at /app
ADD requirements.txt /requirements.txt

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

USER root
RUN apt-get update -y
RUN apt-get install -y python3-dev \
                         gcc \
                         libc-dev \
                         libffi-dev \
                         build-essential \
                         libhdf5-dev
USER airflow
RUN pip install -r /requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV FLASK_APP=api_ann_classifier.py

# Run flask
CMD ["python", "/app/server/api_ann_classifier.py"]