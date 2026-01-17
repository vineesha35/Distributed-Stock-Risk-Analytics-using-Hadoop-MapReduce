# Scalable Financial Market Risk Analytics Using Hadoop MapReduce

## Project Summary

This project demonstrates how large-scale raw stock market data can be transformed into analytics-ready financial datasets using a Hadoop MapReduce pipeline.
The system ingests 7,195 raw stock files, normalizes historical OHLCV data, computes daily returns, and produces consolidated datasets in HDFS that support downstream risk and volatility analysis.
The project highlights scalable data engineering, fault-tolerant batch processing, and financial data preprocessing at scale, solving a core bottleneck faced by financial analytics teams.

---

## Business Problem

Financial institutions and analytics teams face major challenges when working with historical market data:

**Fragmentation**: Market data is split across thousands of per-stock files
**Scale**: Multi-gigabyte datasets cannot be efficiently processed on a single machine
**Unusable Raw Data**: Raw prices cannot directly support risk metrics like returns or volatility
**High Data Preparation Cost**: Most analysis time is spent cleaning and restructuring data

Without a scalable preprocessing pipeline, organizations experience:

**Delayed risk analysis**
**Inconsistent results across teams**
**Inability to scale analytics as data volume grows**
---

## Solution Overview

A two-stage Hadoop MapReduce pipeline was implemented to transform raw stock data into structured, analytics-ready datasets.

The solution:
- Normalizes raw stock price files into a unified OHLCV format
- Computes daily returns per stock using distributed processing
- Stores results in HDFS for scalable access and analysis

This enables efficient downstream financial analysis such as:

- Volatility estimation
- Risk modeling
- Time-series trend analysis
---

## Architecture & Data Flow

Raw Stock Files (7,195 files)
        ↓
HDFS (/market_data/raw/stocks)
        ↓
MapReduce Job 1: Preprocessing
  - Parse raw text files
  - Normalize OHLCV records
        ↓
HDFS (/market_data/processed/normalized)
        ↓
MapReduce Job 2: Returns Calculation
  - Compute daily percentage returns
        ↓
HDFS (/market_data/processed/returns)
        ↓
Python Analytics / Visualization
---

## Technology Stack

- **Big Data Framework:** AApache Hadoop (HDFS + MapReduce), Hadoop Streaming API
- **Programming Language:** Python (Mapper & Reducer logic)
- **Analytics & Visualization:** Pandas (data analysis), Matplotlib / Seaborn (visualization)
- **Environment:** Single-node Hadoop cluster, Windows OS, Local MapReduce execution mode, Python virtual environment
---

## Analytical Outputs

Normalized Dataset

- Clean OHLCV time-series data
- Consolidated into a single distributed output
- Size: ~822 MB
- Stored in HDFS (part-00000)

Returns Dataset

- Daily percentage returns per stock
- Size: ~632 MB
- Enables volatility and trend analysis
---

## Business Insights & Decision Support

### 1.Risk Analysis Enablement
Daily returns provide the foundation for:
- Volatility modeling
- Value-at-Risk (VaR)
- Stress testing\
**Decision enabled:** Risk teams can immediately apply quantitative models without manual preprocessing.

### 2. Scalability Validation
- Successfully processed 7,195 input files using distributed execution
- Demonstrates how financial analytics pipelines scale beyond single-machine limits
**Decision enabled:** Justifies distributed infrastructure investment for historical analysis.

### 3. Operational Efficiency
- Automated data normalization eliminates manual data cleaning
- Reduces analyst preparation time significantly**Decision enabled:** Justifies investment in distributed data processing infrastructure.
**Decision enabled**: Analysts focus on insights instead of data wrangling.

---

## Design Decisions & Trade-offs

- **Why MapReduce:** Works well for batch processing at scale and is fault-tolerant for large historical datasets.
- **Why Streaming + Python:** Allowed rapid development of custom parsing/logic while still leveraging Hadoop execution.
- **Batch-first design:** Optimized for historical risk analysis; real-time monitoring would require streaming architecture.

---


## Limitations & Future Improvements

- **Single-node environment:** Scalable design, but runtime can improve with a multi-node cluster.
- **Batch-only:** Extend to near real-time processing with Kafka/Spark Streaming.
- Rolling volatility and risk metrics (e.g., moving-window volatility)
- Anomaly detection for extreme return spikes
- Cloud storage + orchestration (S3/EMR, Databricks, Airflow)

---

## Repository Structure

```graphql
Scalable-Financial-Risk-Analytics/
├─ data/
│  ├─ raw/                      # (optional) sample raw inputs / references
│  ├─ combined/                 # merged input files (e.g., stocks_all.csv)
│  ├─ processed/                # local processed outputs (optional)
│  └─ sample/                   # small sample dataset for quick tests
├─ src/
│  └─ analytics/
│     ├─ preprocess_mapper.py   # MapReduce #1 mapper (normalize OHLCV)
│     ├─ preprocess_reducer.py  # MapReduce #1 reducer
│     ├─ returns_mapper.py      # MapReduce #2 mapper (compute returns)
│     └─ returns_reducer.py     # MapReduce #2 reducer
├─ notebooks/                   # analysis + plots (optional)
├─ README.md
└─ requirements.txt             # python deps (if used)

