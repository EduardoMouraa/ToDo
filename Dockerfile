FROM python:3.7
ENV PYTHONNUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput