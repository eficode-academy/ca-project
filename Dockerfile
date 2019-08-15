FROM python:3.6-alpine
COPY . /codechan
WORKDIR /codechan
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "run.py"]

EXPOSE 5000
