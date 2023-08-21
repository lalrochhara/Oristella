FROM python:3.10.12

WORKDIR /Oristella
COPY . /Oristella
 
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "Oristella"]
