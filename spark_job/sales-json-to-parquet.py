from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType,
    TimestampType
)
from pyspark.sql.functions import to_date, col

spark = SparkSession.builder \
    .appName("Sales JSON to Parquet (Redshift Compatible)") \
    .getOrCreate()

# -------- Explicit schema --------
sales_schema = StructType([
    StructField("order_id", IntegerType(), True),
    StructField("user_id", IntegerType(), True),
    StructField("product_id", IntegerType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("unit_price", DoubleType(), True),
    StructField("total_amount", DoubleType(), True),
    StructField("payment_type", StringType(), True),
    StructField("order_time", StringType(), True)
])

raw_path = "s3://de-project-raw-sales-aritra/sales/"
curated_path = "s3://de-project-curated-sales-aritra/sales/"

# -------- Read raw JSON --------
df = spark.read \
    .schema(sales_schema) \
    .json(raw_path)

# -------- Transform --------
df = df.withColumn(
    "order_ts",
    col("order_time").cast(TimestampType())
)

df = df.withColumn(
    "sale_date",
    to_date(col("order_ts"))
)

# -------- Data quality --------
df = df.dropna(
    subset=["order_id", "user_id", "product_id", "sale_date"]
)

# Optional: drop intermediate column
df = df.drop("order_ts")

# -------- Write Parquet (NO PARTITIONING) --------
df.write \
    .mode("overwrite") \
    .parquet(curated_path)

spark.stop()
