# docker build -t taxi_ingest::v001 .


# docker run -it \
# --network=pgadmin-network \
# taxi_ingest:v001 \
#    --user=root \
#    --password=root \
#    --host=postgres-test \
#    --port=5432 \
#    --db=ny_taxi \
#    --table_name=green_taxi \
#    --url=${URL} \
#    --cleaning_fun=cleaning_taxi_data

FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app 

COPY ingest_data.py ingest_data.py

ENTRYPOINT ["python", "ingest_data.py"]