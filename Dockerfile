FROM ubuntu:18.04
RUN apt-get update && apt-get install python-pip -y
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]
