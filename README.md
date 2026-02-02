# Real-Time Sales Analytics Pipeline (AWS + PySpark + Redshift)

This project implements an end-to-end data engineering pipeline that ingests mock e-commerce data, transforms it using PySpark on AWS Glue, and loads it into Amazon Redshift for analytics and BI use cases.

The pipeline is designed to be **cost-efficient**, **modular**, and **production-inspired**, while remaining simple enough for local testing and learning.

---

## Architecture Overview

**Data Flow:**

Generators → Amazon S3 (RAW) → PySpark (AWS Glue) → Amazon S3 (CURATED) → Amazon Redshift → Analytics / BI

**Storage Strategy:**
- Small dimension tables (users, products): JSON → Redshift
- Fact table (sales): JSON → Parquet → Redshift

---

## Tech Stack

- **Python** (data generators)
- **Apache Spark (PySpark)** via AWS Glue
- **Amazon S3** (raw + curated layers)
- **Amazon Redshift (Provisioned / RA3)**
- **IAM (role-based access)**
- **SQL (analytics queries)**

---

## Project Structure
.
├── producers/
│ ├── user_generator.py
│ ├── product_generator.py
│ └── sales_generator.py
│
├── spark_jobs/
│ └── sales_json_to_parquet.py
│
├── docs/
│ ├── aws-setup.md
│ ├── run-manual.md
│ └── config.md
│
└── README.md
---

## 📊 Data Model (Star Schema)

### Dimension Tables
- `dim_users`
- `dim_products`

### Fact Table
- `fact_sales`

---

## 🧠 Key Design Decisions

- **JSON used for dimensions** for schema flexibility and robust loading.
- **Parquet used for facts** for analytical performance.
- **No Spark partitioning** in curated data loaded into Redshift (schema alignment).
- **Explicit schemas** enforced in Spark jobs.
- **RAW data preserved** for replayability.

---

## Documentation

- 👉 [`docs/aws-setup.md`](docs/aws-setup.md) — AWS setup & IAM
- 👉 [`docs/run-manual.md`](docs/run-manual.md) — How to run the pipeline
- 👉 [`docs/config.md`](docs/config.md) — Configuration & assumptions

---

## Future Improvements

- Incremental fact loads
- Data quality checks
- Airflow orchestration
- BI dashboards (Tableau)

---

## Author

Built by **Aritra Lahiri** as a hands-on Data Engineering project focusing on real-world AWS + Spark challenges.

