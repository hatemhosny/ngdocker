FROM python

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN mkdir /backend

COPY . /backend

WORKDIR /backend

CMD ["python", "api.py"]
