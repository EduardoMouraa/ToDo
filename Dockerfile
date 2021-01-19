FROM python:3.7
ENV PYTHONNUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.txt
RUN pip install -r requirements.txt