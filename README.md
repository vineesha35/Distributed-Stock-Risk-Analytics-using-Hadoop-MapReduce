# Scalable Financial Market Risk Analytics Using Hadoop MapReduce

## Executive Summary

Financial institutions ingest massive volumes of high-frequency market data that must be processed efficiently to support risk monitoring, infrastructure planning, and market analysis.

This project demonstrates how Hadoop MapReduce can be used to transform raw, high-volume stock exchange data (10GB+) into structured, analytics-ready datasets that enable:
- Market risk quantification
- Identification of high-volatility periods
- Operational capacity planning for trading systems

The solution showcases scalable data engineering, statistical analysis, and business-focused insights derived from big data.

## Business Problem

Stock exchanges and financial institutions face three key challenges:

1. **Volume** – Multi-gigabyte, high-frequency time-series data that cannot be processed efficiently on a single machine.
2. **Velocity** – Rapid data generation requiring scalable batch processing.
3. **Decision Latency** – Raw data is unusable for risk analysis without aggregation and transformation.

Without scalable processing pipelines, organizations risk:
- Delayed risk detection
- Poor infrastructure capacity planning
- Missed insights during volatile market events

## Solution Overview

A custom Hadoop MapReduce pipeline was implemented to process raw stock exchange data and generate clean, aggregated time-series outputs.

The pipeline:
- Parses and cleans raw transaction-level data
- Aggregates price and transaction counts per time interval
- Produces analytics-ready datasets suitable for downstream statistical analysis and visualization

The final dataset enables rapid analysis of volatility, trading patterns, and operational load characteristics.

## Architecture & Data Flow

Raw Stock Data (10GB+)
        ↓
Hadoop HDFS
        ↓
Mapper: Parse & Extract (timestamp, price)
        ↓
Reducer: Aggregate (total price, count, average)
        ↓
Clean Time-Series Dataset
        ↓
Python Analytics & Visualization

## Technology Stack

- **Big Data Framework:** Apache Hadoop MapReduce
- **Programming Language:** Python (Streaming API for Mapper & Reducer)
- **Analytics & Visualization:** Python (Pandas, Matplotlib, Seaborn)
- **Environment:** Single-node Hadoop cluster (Local / Cloud VM)

## Analytical Outputs

The MapReduce pipeline reduced raw multi-gigabyte input data to **8,072 clean aggregated records**, enabling fast downstream analysis.

Key derived metrics include:
- Average price per time interval
- Trading activity volume
- Rolling volatility measures

## Business Insights & Decision Support

### 1. Market Risk Monitoring
30-day rolling volatility analysis highlights periods of extreme market instability, often aligned with macroeconomic or external events.
**Decision enabled:** Risk teams can increase monitoring or adjust exposure during high-volatility periods.

### 2. Infrastructure & Capacity Planning
Trading activity patterns by day-of-week reveal consistent peak loads (Mon–Fri).
**Decision enabled:** Infrastructure teams can allocate compute resources more efficiently during high-traffic windows.

### 3. Big Data Value Demonstration
The project demonstrates how MapReduce enables massive data reduction while preserving critical analytical signals.
**Decision enabled:** Justifies investment in distributed data processing infrastructure.

## Design Decisions & Trade-offs

- **Why MapReduce:** Chosen for scalability and fault tolerance when processing large batch datasets.
- **Why Batch Processing:** Suitable for historical risk analysis; real-time streaming would require a different architecture (e.g., Spark/Kafka).
- **Single-Node Cluster:** Used for cost and development simplicity; architecture is horizontally scalable.

## Limitations & Future Improvements

- Extend to multi-node Hadoop or Spark for improved performance
- Introduce streaming ingestion for near real-time risk monitoring
- Integrate cloud-native storage and orchestration (e.g., AWS S3, EMR)
- Add anomaly detection for automated risk alerts

## Repository Structure

- `mapper.py` – Parses raw stock data and emits (time_key, price, count)
- `reducer.py` – Aggregates total price, transaction count, and average price
- `visualizations.ipynb` – Statistical analysis and visualizations built on MapReduce outputs

