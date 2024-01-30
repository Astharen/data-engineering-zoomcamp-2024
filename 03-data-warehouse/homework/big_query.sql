-- Setup
CREATE OR REPLACE EXTERNAL TABLE `terraform-412019.nytaxi.green_data`
OPTIONS (
  format = 'parquet',
  uris = ['gs://mage-zoomcamp-123456/green_taxi_data.parquet']
);

CREATE OR REPLACE TABLE terraform-412019.nytaxi.green_data_non_partitoned AS
SELECT * FROM terraform-412019.nytaxi.external_green_data;


-- Question 1

SELECT COUNT(*) 
FROM terraform-412019.nytaxi.external_green_data;

-- Question 2

SELECT DISTINCT(PULocationID)
FROM terraform-412019.nytaxi.external_green_data;


SELECT DISTINCT(PULocationID)
FROM terraform-412019.nytaxi.green_data_non_partitoned;

-- Question 3

SELECT COUNT(fare_amount) 
FROM `terraform-412019.nytaxi.green_data_non_partitoned`
WHERE fare_amount = 0;

-- Question 4

CREATE OR REPLACE TABLE `terraform-412019.nytaxi.green_data_partitoned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM `terraform-412019.nytaxi.green_data_non_partitoned`;


-- Question 5

SELECT DISTINCT(PULocationID)
FROM `terraform-412019.nytaxi.green_data_non_partitoned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';


SELECT DISTINCT(PULocationID)
FROM `terraform-412019.nytaxi.green_data_partitoned_clustered`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';