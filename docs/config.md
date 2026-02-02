## General Assumptions

- This is a **learning / demo project**, not production
- Data volumes are intentionally small
- Pipeline is manually triggered

---

## Data Format Choices

| Dataset | Format | Reason |
|------|------|------|
| users | JSON | Small dimension, flexible |
| products | JSON | Small dimension, flexible |
| sales | Parquet | Fact table, analytics |

---

## Spark Design

- Explicit schemas used
- No filesystem partitioning for curated data loaded into Redshift
- Helper columns removed before write

---

## Redshift Design

- Star schema
- `DISTSTYLE ALL` for dimensions
- `DISTKEY + SORTKEY` for fact table
- No Glue Catalog dependency

---

## Cost Considerations

- Glue jobs run only on demand
- No streaming services used
- Redshift single-node cluster
