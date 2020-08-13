FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y \
    python3 \
    python3-pip \
    python3-flask \
    python3-flask-sqlalchemy \
    wget && apt-get clean

RUN pip3 install Flask-WTF
RUN pip3 install Flask
    
COPY . /app

WORKDIR /app



ENTRYPOINT [ "python3", "run.py" ]