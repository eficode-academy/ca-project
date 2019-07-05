FROM yagoor/ca-project

# Copy project files
COPY create_db.py run.py config.py $PROJECT_DIRECTORY/

# Copy project files
COPY app $PROJECT_DIRECTORY/app

# Create the database
RUN python $PROJECT_DIRECTORY/create_db.py

# Run the application
CMD ["sh", "-c", "python $PROJECT_DIRECTORY/run.py"]
