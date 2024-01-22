# It is run from the folder that contains the docker file (2_docker_sql) 
# with docker build -t <name>:<version> <directory>

# Once created, docker run -it <name>:<version>
# (not necessary to add bash since it's included as entrypoint I guess)
FROM python:3.9 
# From this docker image

RUN pip install pandas 
# Run this command (in linux bash)

WORKDIR /app 
# The working directory where will be the script
COPY pipeline.py pipeline.py
# Copy the file pipeline.py in pipeline.py

ENTRYPOINT ["python", "pipeline.py"]
# Entrypoint ["bash"] when you enter, it will be at the terminal
# Entrypoint ["python", "pipeline.py"] to run the script