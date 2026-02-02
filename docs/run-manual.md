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

## STEP 2 — Verify RAW Data in S3