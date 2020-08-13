FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y \
    pip3 \
    python3 \
    sqlalchemy
