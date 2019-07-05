FROM python:2.7.16

# Set env variable to keep file clean
ENV PROJECT_DIRECTORY /python

# Copy requirements into project
COPY requirements.txt $PROJECT_DIRECTORY/ 

# Install requirements
RUN pip install -r $PROJECT_DIRECTORY/requirements.txt

# Copy project files
COPY create_db.py run.py config.py $PROJECT_DIRECTORY/

# Copy project files
COPY app $PROJECT_DIRECTORY/app

# Create the database
RUN python $PROJECT_DIRECTORY/create_db.py

# Run the application
CMD ["sh", "-c", "python $PROJECT_DIRECTORY/run.py"]
