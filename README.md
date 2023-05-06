# Covid-data-fetch-bigquery-airflow

This repository contains codes to fetch COVID-19 data from an external API and store them into Google BigQuery using Apache Airflow. The repository provides a dag.py file that sets up an Airflow DAG to run the data fetching and storing process on a schedule.

## Installation

To install the necessary packages, run the following command:

    pip install -r requirements.txt

## Configuration

Before running the code, make sure to configure the following variables in the dag.py file:

- `PROJECT_ID`: the ID of the Google Cloud project
- `DATASET_NAME`: the name of the BigQuery dataset to store the data in
- `TABLE_NAME`: the name of the BigQuery table to store the data in
- `API_URL`: the URL of the external API to fetch the data from

## Contributing

Contributions to this repository are welcome. If you find a bug or have a suggestion for improvement, please feel free to open an issue or a pull request.
