# function to fetch the case data
def fetch_cases():
    # request to the API to get the case data
    response = requests.get('https://api.covid19api.com/dayone/country/india/status/confirmed')
    data = response.json()

    # Extract the relevant fields from the data
    cases = []
    for record in data:
        date = record['Date']
        cases = record['Cases']
        cases.append({'date': date, 'cases': cases})

    return cases


# Define a function to save the case data to BigQuery
def save_cases(**kwargs):
    # Extract the case data from the kwargs
    cases = kwargs['ti'].xcom_pull(task_ids='fetch_cases')

    # Create a BigQuery client
    client = bigquery.Client()

    # Create a new dataset
    dataset = bigquery.Dataset(client.dataset('covid_data'))
    dataset.location = 'US'
    dataset = client.create_dataset(dataset)

    # Create a new table in the dataset
    table = bigquery.Table(dataset.table('case_data'), schema=[
        bigquery.SchemaField('date', 'DATE'),
        bigquery.SchemaField('cases', 'INTEGER')
    ])
    table = client.create_table(table)

    # Load the data into the table
    errors = client.insert_rows(table, rows=cases)
    if errors:
        print(errors)
