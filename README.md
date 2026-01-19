# Scalable Financial Market Risk Analytics Using Hadoop MapReduce

## Project Summary
This project demonstrates how large-scale, fragmented historical stock-market data can be transformed into **analytics-ready financial datasets** using a **Hadoop MapReduce** pipeline. The system ingests **7,195 raw stock files** from HDFS, normalizes historical **OHLCV** time-series records, computes **daily returns**, and produces consolidated outputs in HDFS to support downstream **risk and volatility analysis**. The project highlights scalable data engineering, fault-tolerant batch processing, and financial preprocessing at scale—addressing a core bottleneck for financial analytics teams.

---

## Business Problem
Financial institutions and analytics teams face major challenges when working with historical market data:

- **Fragmentation:** Market data is split across thousands of per-stock files, making it hard to process consistently.
- **Scale:** Multi-gigabyte datasets are expensive and slow to process on a single machine.
- **Raw Data Limitations:** Raw prices do not directly support risk metrics such as returns or volatility.
- **High Preparation Cost:** A large portion of analysis time is spent cleaning, restructuring, and standardizing data.

Without a scalable preprocessing pipeline, organizations experience:
- **Delayed risk analysis**
- **Inconsistent preprocessing and results across teams**
- **Inability to scale analytics as data volume increases**

---

## Solution Overview
A **two-stage Hadoop MapReduce pipeline** was implemented to transform raw stock data into structured, analytics-ready datasets.

The pipeline:
- Normalizes raw stock price files into a unified **OHLCV** format
- Computes **daily percentage returns**
- Stores results in **HDFS** for scalable access and reuse

This enables downstream analysis such as:
- Volatility estimation
- Risk modeling (VaR / stress testing inputs)
- Time-series trend analysis

---

## Architecture & Data Flow

**Raw Stock Files (7,195 files)**  
→ **HDFS** (`/market_data/raw/stocks`)  
→ **MapReduce Job 1: Preprocessing / Normalization**  
&nbsp;&nbsp;• Parse raw text files  
&nbsp;&nbsp;• Standardize to OHLCV schema  
→ **HDFS** (`/market_data/processed/normalized`)  
→ **MapReduce Job 2: Returns Calculation**  
&nbsp;&nbsp;• Compute daily percentage returns from OHLCV  
→ **HDFS** (`/market_data/processed/returns`)  
→ **Python Analytics & Visualization** (Jupyter / reports)

---

## Technology Stack
- **Big Data Framework:** Apache Hadoop (**HDFS + MapReduce**), Hadoop Streaming API  
- **Programming Language:** Python (mapper & reducer logic)  
- **Analytics & Visualization:** Pandas, Matplotlib / Seaborn  
- **Environment:** Single-node Hadoop cluster (Windows), MapReduce local execution mode, Python virtual environment  

---

## Analytical Outputs

### Normalized Dataset
- Cleaned and standardized OHLCV time-series records
- Consolidated output written to HDFS (example: `part-00000`)
- **Size:** ~822 MB
- **Location:** `/market_data/processed/normalized`

### Returns Dataset
- Daily percentage returns derived from normalized OHLCV
- **Size:** ~632 MB
- **Location:** `/market_data/processed/returns`

---

## Business Insights & Decision Support

### 1. Risk Analysis Enablement
Daily returns provide the foundation for:
- Volatility modeling
- Value-at-Risk (VaR)
- Stress testing inputs

**Decision enabled:** Risk teams can immediately apply quantitative models without manual preprocessing.

### 2. Scalability Validation
- Successfully processed **7,195 input files** using Hadoop-based batch processing
- Demonstrates a pipeline that scales beyond single-machine workflows

**Decision enabled:** Supports investment in distributed infrastructure for historical risk analytics.

### 3. Operational Efficiency
- Automated normalization reduces manual cleaning and restructuring
- Standardized outputs improve repeatability and collaboration across analysts

**Decision enabled:** Analysts focus more on insights and modeling, less on data wrangling.

---

## Design Decisions & Trade-offs
- **Why MapReduce:** Strong fit for fault-tolerant batch processing over large historical datasets.
- **Why Hadoop Streaming + Python:** Rapid development of custom logic while still leveraging Hadoop execution.
- **Batch-first design:** Optimized for historical analysis; near real-time monitoring would require a streaming architecture.

---

## Limitations & Future Improvements
- **Single-node environment:** Pipeline is scalable by design, but runtime would improve on a multi-node cluster.
- **Batch-only processing:** Extend to near real-time ingestion and monitoring using Kafka / Spark Streaming.
- Add rolling-window metrics (e.g., 30-day volatility, drawdowns)
- Add anomaly detection for extreme return spikes
- Integrate cloud-native storage + orchestration (AWS S3/EMR, Databricks, Airflow)

---

## Repository Structure
```text
Scalable-Financial-Risk-Analytics/
├─ data/
│  ├─ raw/                      # optional: sample raw inputs / references
│  ├─ combined/                 # merged input files (exclude large files from GitHub)
│  ├─ processed/                # optional: local processed outputs
│  └─ sample/                   # small dataset for quick tests
├─ src/
│  ├─ preprocessing/
│  │  ├─ preprocess_mapper.py   # MapReduce Job 1 mapper (normalize OHLCV)
│  │  └─ preprocess_reducer.py  # MapReduce Job 1 reducer
│  └─ analytics/
│     ├─ returns_mapper.py      # MapReduce Job 2 mapper (compute returns)
│     ├─ returns_reducer.py     # MapReduce Job 2 reducer
│     ├─ volatility_mapper.py   # optional: volatility job mapper
│     ├─ volatility_reducer.py  # optional: volatility job reducer
│     ├─ topk_mapper.py         # optional: top-k movers mapper
│     └─ topk_reducer.py        # optional: top-k movers reducer
├─ notebooks/                   # Jupyter notebooks for analysis/plots (optional)
├─ plots/                       # generated figures/screenshots (optional)
├─ README.md
└─ requirements.txt
