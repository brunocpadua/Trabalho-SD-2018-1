FROM python:2
ADD Consumidor.py /
ADD Produtor.py /
RUN pip install pika
RUN pip install progressbar2
