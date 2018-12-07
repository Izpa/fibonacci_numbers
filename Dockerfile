FROM python:3.6

WORKDIR /app

ADD . /app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "gunicorn_run:app"]