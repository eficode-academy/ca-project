FROM ubuntu:18.04
COPY . / 
RUN apt-get update -y && apt-get install -y \ 
    python \ 
    python-pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]