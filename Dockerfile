FROM python:2
RUN apt-get update && apt-get install python-pip -y
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "run.py"]
