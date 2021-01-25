FROM python:3.7
ENV PYTHONNUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN /usr/local/bin/python3 -m pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/