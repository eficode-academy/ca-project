FROM python


ADD dist/codechan-*.tar.gz /

RUN pip3 install -r requirements.txt

ENTRYPOINT python3 run.py
