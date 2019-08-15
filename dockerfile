FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install python-pip -y 
RUN pip install requests
COPY ./ /pythonweb
EXPOSE 5000
CMD pip install -r /pythonweb/requirements.txt && python /pythonweb/run.py 

