FROM ubuntu:latest
RUN apt-get update 
RUN apt install python3 -y
RUN apt install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]
CMD ["run.py"]