FROM python:2.7.18
EXPOSE 5555

COPY sources.list /etc/apt/
RUN apt-get update && apt-get install -y socat
WORKDIR /app
COPY main.py .

CMD ["python2", "/app/main.py"]
