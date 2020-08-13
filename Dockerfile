FROM ubuntu:latest

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN git clone https://github.com/praqma-training/ca-project.git

COPY ./requirements.txt /ca-project/

RUN pip3 install -r /ca-project/requirements.txt

ENTRYPOINT ["python3", "/ca-project/run.py"]




