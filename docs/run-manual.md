# Manual Run Guide

This document explains how to run the pipeline step by step.

---

## STEP 1 — Generate RAW Data

Run generators locally:

```bash
python producers/user_generator.py
python producers/product_generator.py
python producers/sales_generator.py

1. Users & products are finite
2. Sales runs continuously (stop after a few minutes)

---

## STEP 2 — Verify RAW Data in S3
Check that JSON files exist under:

s3://de-project-raw-sales-aritra/

## STEP 3 — Run Spark Jobs (AWS Glue)

1. Run Glue job
2. Sales Spark job

Ensure jobs succeed and Parquet is generated for sales.

## STEP 4 — Load Dimensions into Redshift

COPY dim_users
FROM 's3://de-project-raw-sales-aritra/users/'
IAM_ROLE 'arn:aws:iam::<ACCOUNT_ID>:role/de-analytics-role'
FORMAT AS JSON 'auto';

COPY dim_products
FROM 's3://de-project-raw-sales-aritra/products/'
IAM_ROLE 'arn:aws:iam::<ACCOUNT_ID>:role/de-analytics-role'
FORMAT AS JSON 'auto';


## STEP 5 — Load Fact Table

COPY fact_sales
FROM 's3://de-project-curated-sales-aritra/sales/'
IAM_ROLE 'arn:aws:iam::<ACCOUNT_ID>:role/de-analytics-role'
FORMAT AS PARQUET;

## STEP 6 — Validate

SELECT
  f.order_id,
  f.sale_date,
  u.city,
  p.category,
  f.total_amount
FROM fact_sales f
JOIN dim_users u ON f.user_id = u.user_id
JOIN dim_products p ON f.product_id = p.product_id
LIMIT 10;
