FROM aliarf/codechan:1.0
MAINTAINER  Ali Arfan "s301599@stud.hioa.no"


COPY . .
RUN pip install -r requirements.txt
CMD ["python", "run.py"]

EXPOSE 5000
RUN echo " Codechan is running nyaaah~"  

