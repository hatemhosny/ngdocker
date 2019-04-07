FROM python:3.7.2-alpine

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir backend

COPY . ./backend

WORKDIR /backend

EXPOSE 80

# CMD ["gunicorn", "api:api", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "80"]
