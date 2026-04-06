# Terraform – GCP Infrastructure Setup

This module contains Terraform configuration used to provision cloud infrastructure on **Google Cloud Platform (GCP)** as part of my Data Engineering Zoomcamp project.

---

## Overview

Using Terraform (Infrastructure as Code), this setup automatically creates:

- 📦 Google Cloud Storage (GCS) Bucket  
- 🧠 BigQuery Dataset  

This allows scalable and reproducible cloud infrastructure for data engineering pipelines.

---

## Architecture


Terraform → GCP
├── GCS Bucket (data storage)
└── BigQuery Dataset (data warehouse)


---

## Project Structure


terraform/
├── main.tf # Main Terraform configuration
├── variables.tf # Input variables
├── terraform.lock.hcl # Provider lock file
├── variables.tfvars.example # Example variables file
├── .gitignore # Ignore sensitive files
└── README.md # Documentation


---

## Prerequisites

Before running this setup, ensure you have:

- Terraform installed
- Google Cloud SDK installed
- A GCP project created
- Service account with appropriate permissions

---

## Authentication Setup

1. Create a service account in GCP  
2. Download the JSON key file  
3. Set environment variable: