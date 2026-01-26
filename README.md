# Real-Time Data Engineering Pipeline on AWS

## Project Overview
This project simulates a real-world data engineering pipeline for processing streaming social media activity and e-commerce transactions using a serverless cloud architecture.

The pipeline demonstrates ingestion, transformation, storage, warehousing, and visualization of real-time data.

---

## Architecture

Data Sources → Streaming → Data Lake → Data Warehouse → BI Dashboard

- **Data Sources**: Sales Generator (Python), Social Media API
- **Streaming**: AWS Kinesis
- **Processing**: AWS Lambda / Spark Streaming
- **Storage**: Amazon S3 (Parquet)
- **Warehouse**: Amazon Redshift
- **Visualization**: Tableau

## Data Warehouse Design

This project follows a **star schema** model:

- **fact_sales**: Stores transactional data
- **dim_users**: Stores user attributes
- **dim_products**: Stores product metadata

This enables efficient analytical queries and reporting.

---

## Phase 1: Data Source Simulation

### Sales Data Generator
A Python script that simulates real-time e-commerce transactions including:
- Order ID
- User ID
- Product ID
- Price
- Quantity
- Payment Type
- Timestamp

This simulates a production transaction system for streaming ingestion.

---

## Tech Stack
Python, AWS Kinesis, AWS Lambda, S3, Redshift, Tableau, Parquet, SQL

---

## Future Phases
- Streaming ingestion with Kinesis
- ETL processing and data lake storage
- Redshift data warehouse
- BI dashboard in Tableau
