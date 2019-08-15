FROM python
COPY . / 
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]