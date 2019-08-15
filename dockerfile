FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install python-pip -y 
RUN pip install requests -y
COPY ./ /pythonweb
CMD pip install -r requirements.txt && python /pythonweb/run.py 

