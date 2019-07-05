#Base image
FROM ubuntu:18.04

COPY * /usr/src/app/
COPY app/ /usr/src/app/app/
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
EXPOSE 5000

CMD ["python", "/usr/src/app/run.py"]

