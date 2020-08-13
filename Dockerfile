FROM python


ADD dist/codechan-*.tar.gz /opt

WORKDIR /opt/codechan-0.1.1
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 run.py
#CMD ["bash"]
