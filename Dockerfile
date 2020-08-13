FROM python

COPY requirements.txt run.py config.py /
COPY app /app

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 run.py