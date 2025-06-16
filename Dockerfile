# Use official Python image
FROM python:3.12-alpine


LABEL maintainer="ali.ahadi.official@gmail.com"


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt . 

# Copy core application files
COPY /app /app/


# Install system dependencies required for psycopg2


# Copy the rest of the application files


# Install dependencies
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user

USER django-user     