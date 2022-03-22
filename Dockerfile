FROM python:3.10

WORKDIR /monitor

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python3", "main/arcteryx.py"]