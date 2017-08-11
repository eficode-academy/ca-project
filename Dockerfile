FROM aliarf/codechan:1.0
MAINTAINER  Ali Arfan "s301599@stud.hioa.no"


COPY . .
RUN pip install -r requirements.txt
RUN python run.py

RUN echo " Codechan is running nyaaah~"  

