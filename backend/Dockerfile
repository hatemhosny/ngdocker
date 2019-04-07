FROM python

COPY requirements.txt /

RUN pip install -r requirements.txt

ADD . /backend

EXPOSE 80

WORKDIR /backend

# CMD ["gunicorn", "api:api", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
CMD ["python", "api.py"]