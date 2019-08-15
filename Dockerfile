FROM python:2
COPY . / 
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]