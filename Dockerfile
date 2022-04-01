FROM python:3.10
WORKDIR /monitor
COPY . .
RUN pip install -r requirements.txt
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python3", "main/arcteryx.py"]