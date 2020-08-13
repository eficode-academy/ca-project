FROM python:3.7-alpine
COPY . /usr/src/app/
RUN pip3 install -r /usr/src/app/requirements.txt
EXPOSE 5000
CMD ["python3", "/usr/src/app/run.py"]
