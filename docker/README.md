# Data Engineering Pipeline – NYC Taxi Data

This project is part of my learning journey of the **DataTalks.Club Data Engineering Zoomcamp.**
It demonstrates building a simple data pipeline to ingest NYC taxi trip data into PostgreSQL using Docker.

---

## Project Overview

The pipeline:
- Downloads NYC taxi data (CSV)
- Processes it in chunks using pandas
- Loads it into PostgreSQL
- Uses Docker for reproducibility

---

## Features

- Chunked data ingestion (memory efficient)
- Dockerized pipeline
- CLI-based configuration
- PostgreSQL integration

## Tech Stack

- Python
- Pandas
- PostgreSQL
- Docker & Docker Compose
- SQLAlchemy
- Click (CLI)
- PyArrow

---

## Project Structure

```text
.
├── Dockerfile               # Instructions to containerize the ingestion script
├── docker-compose.yaml      # Orchestrates Postgres and pgAdmin services
├── ingest_data.py           # Main Python script for data ingestion logic
├── pipeline.py              # Auxiliary pipeline logic
├── main.py                  # Entry point
├── notebook.ipynb           # Exploratory Data Analysis and testing
├── pyproject.toml           # Project dependencies and metadata
└── uv.lock                  # Locked dependency versions
```

## Prerequisites

- Python 3.13 or higher  
- Docker and Docker Compose  
- Git  

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Eyyub0491/data-engineering-zoomcamp.git
cd data-engineering-zoomcamp
```

### 2. Set up the Python environment (for the pipeline)

```bash
cd pipeline
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

### 3.Start the database services:

```bash
docker-compose up -d
pip install -r requirements.txt
```

## Usage

Ingest Data
-To ingest NYC yellow taxi data into the database:

```bash
cd pipeline
python ingest_data.py --year 2021 --month 1 --pg-host localhost
```
- --year and --month: Specify the year and month for the data (default: 2021-01)
- --pg-user, --pg-pass, --pg-host, --pg-port, --pg-db: Database connection details (defaults provided)
- --target-table: Target table name (default: yellow_taxi_data)
- --chunksize: Number of rows to process at once (default: 100000)
