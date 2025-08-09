# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS tthdatabricksdev.audit;
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS tthdatabricksdev.audit.load_logs (
# MAGIC     id BIGINT GENERATED ALWAYS AS IDENTITY,
# MAGIC     data_source STRING,
# MAGIC     tablename STRING,
# MAGIC     numberofrowscopied INT,
# MAGIC     watermarkcolumnname STRING,
# MAGIC     loaddate TIMESTAMP
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC truncate table  tthdatabricksdev.audit.load_logs 

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from audit.load_logs
