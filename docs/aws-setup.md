# AWS Setup Guide

This document describes the one-time AWS setup required to run the pipeline.

---

## 1. IAM Role

Create an IAM role (e.g. `de-analytics-role`) with the following permissions:

- Amazon S3 read/write access to:
  - raw bucket
  - curated bucket
- AWS Glue permissions (Spark jobs)
- Amazon Redshift COPY permissions

The role must be attached to:
- AWS Glue jobs
- Amazon Redshift cluster

---

## 2. Amazon S3 Buckets

Create two buckets (or prefixes):

### RAW layer
s3://de-project-raw-sales-aritra/
├── users/
├── products/
└── sales/


### CURATED layer
s3://de-project-curated-sales-aritra/
└── sales/

---

## 3. AWS Glue

- Glue version: **4.0**
- Job type: **Spark (PySpark)**
- Worker type: `G.1X`
- Workers: 2

Each dataset has its own Spark job.

---

## 4. Amazon Redshift

- Type: Provisioned cluster
- Node type: `ra3.large`
- Nodes: 1
- Database: `analytics`
- Public access enabled (for BI tools)

---

## 5. Network Configuration

Ensure:
- Redshift security group allows inbound traffic on port `5439`
- IAM role is attached to Redshift cluster