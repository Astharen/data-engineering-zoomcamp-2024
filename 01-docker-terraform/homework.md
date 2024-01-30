## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment 
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker 

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits* 

- `--delete`
- `--rc`
- `--rmc`
- `--rm` -> This one


## Question 2. Understanding docker first run 

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ). 

What is version of the package *wheel* ?

- 0.42.0 -> This one
- 1.0.0
- 23.0.1
- 58.1.0


# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## Question 3. Count records 

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18. 

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.


Query: ```SELECT count(*) FROM green_taxi WHERE lpep_pickup_datetime >= '2019-09-18 00:00:00' AND lpep_pickup_datetime < '2019-09-19 00:00:00' AND lpep_dropoff_datetime >= '2019-09-18 00:00:00' AND lpep_dropoff_datetime < '2019-09-19 00:00:00'```

- 15767
- 15612 -> This one
- 15859
- 89009

## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

Query: ```SELECT DATE(lpep_pickup_datetime) AS datetime, SUM(trip_distance) as sum_dist FROM green_taxi GROUP BY datetime ORDER BY sum_dist DESC LIMIT 1``` or
```SELECT lpep_pickup_datetime, trip_distance FROM green_taxi ORDER BY trip_distance DESC LIMIT 1```

- 2019-09-18
- 2019-09-16
- 2019-09-26 -> This one with the largest trip
- 2019-09-21


## Question 5. The number of passengers

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

Query: 
```SELECT DATE(gt.lpep_pickup_datetime) as pickup_day, tz."Borough", SUM(gttotal_amount) AS total_sum FROM green_taxi AS gtJOIN taxi_zone AS tz ON tz."LocationID" = gt."PULocationID" where DATE(gt.lpep_pickup_datetime) = '2019-09-18' GROUP BY pickup_day, tz."Borough" HAVING SUM(gt.total_amount) > 50000 AND tz."Borough" != 'Unknown'```
 
- "Brooklyn" "Manhattan" "Queens" -> This one
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens" 
- "Brooklyn" "Queens" "Staten Island"


## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

Query: ```SELECT tz."Zone" from (SELECT gt."DOLocationID" FROM green_taxi AS gt JOIN taxi_zone AS tz ON tz."LocationID" = gt."PULocationID" WHERE tz."Zone" = 'Astoria' and DATE_TRUNC('month', gt.lpep_pickup_datetime)::date = '2019-09-01' ORDER BY gt.tip_amount DESC LIMIT 1) as t JOIN taxi_zone AS tz ON tz."LocationID" = t."DOLocationID"```

- Central Park
- Jamaica
- JFK Airport -> This one
- Long Island City/Queens Plaza



## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.

google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 1s [id=projects/terraform-412019/datasets/demo_dataset]
google_storage_bucket.demo-bucket: Creation complete after 1s [id=terraform-412019-terra-bucket]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.



## Submitting the solutions

* Form for submitting: 
* You can submit your homework multiple times. In this case, only the last submission will be used. 

Deadline: 29 January, 23:00 CET