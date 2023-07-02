FROM python:3.9.6-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /yogesh_application
COPY . /yogesh_application
RUN pip install -r requirements.txt
