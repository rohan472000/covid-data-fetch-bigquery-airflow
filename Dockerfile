FROM python:3.10

RUN pip install requests
RUN pip install pip install python-csv

# Copy the code into the image
COPY covid_fetch_local.py .

# Set the working directory
WORKDIR .

CMD ["python", "covid_fetch_local.py"]
