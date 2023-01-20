FROM python:3.9.10

WORKDIR /oldtagger.py

COPY . /oldtagger.py

 

RUN pip3 install -U pip

COPY requirements.txt .

RUN pip3 install -U -r requirements.txt

CMD ["python3", "oldtagger.py"]
