FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/backend
WORKDIR /app/backend
COPY . /app/backend
RUN pip install -r requirements.txt

EXPOSE 6000