# FX Prediction

## Overview

**FX Prediction** is a research-oriented data pipeline designed to analyze how global news and macroeconomic events influence the **EUR/USD exchange rate**.
It combines structured financial time series with standardized news and event metadata, enabling future modeling of relationships between sentiment, policy, and market movement.

The project emphasizes **modularity, test-driven development (TDD), and data transparency** throughout the pipeline.

---

## Project Structure

```
fx-prediction/
│
├── scripts/
│   ├── api_calls/
│   │   ├── contextualweb_fetch.py        # Modular API fetch functions
│   │   ├── standardize_responses.py      # Defines NewsItem model and response converters
│   │
│   ├── data_pipeline/
│   │   ├── forex_loader.py               # Loads and standardizes local forex data
│   │   ├── news_pipeline.py              # Main pipeline for fetching, enriching, aligning news
│   │
│   └── __init__.py
│
├── data/
│   ├── raw/                              # Local forex .txt files in varying granularities
│   ├── external/                         # News, GDELT, and archive data
│   └── processed/                        # Standardized, aligned datasets for modeling
│
├── tests/
│   ├── fixtures/                         # Mock JSON and forex samples for testing
│   ├── test_forex_loader.py              # Unit tests for forex file parsing
│   ├── test_news_pipeline.py             # Tests for pipeline and data alignment
│   └── test_standardize_responses.py     # Tests for standardized news formatting
│
├── models/                               # Reserved for trained models and results
│
├── requirements.txt
├── README.md
└── main.py
```

---

## Pipeline Description

### 1. Keyword Selection

Relevant economic and geopolitical terms (e.g., “EUR/USD”, “ECB”, “interest rates”, “inflation”) are defined for querying.

### 2. News Retrieval

News metadata is fetched from structured sources such as **GDELT** using modular API clients.

### 3. Standardization

Raw results are normalized through the `NewsItem` model, creating a unified format across APIs and archives.

### 4. Archival Enrichment

Article text is retrieved from archives (e.g., the Wayback Machine) to complement metadata with content-based insights.

### 5. Forex Data Loading

Locally stored forex data (.txt, CSV-format) is parsed and timestamped at various granularities (daily, hourly, minute-level) via the Forex DataLoader `ForexLoader`.

### 6. Alignment

News and forex datasets are aligned by time windows to prepare for correlation analysis and predictive modeling.

---

## Technical Highlights

* **Language & Tools**: Python (pandas, pytest, pathlib, typing)
* **Architecture**: Modular, object-oriented, environment-driven design
* **Testing**: Test-driven development using **pytest** and isolated fixtures
* **Data Handling**: Flexible loaders for multi-granularity forex data and JSON news sources
* **Extensibility**: Easily integrates additional APIs or model training components
* **Reproducibility**: Separation of raw, external, and processed data ensures full traceability

---

## Future Directions

* Integration of sentiment and topic modeling (NLP-based analysis)
* Event-based correlation with central bank communications
* Feature engineering for predictive time series models
* Development of forecasting and classification models
* Visualization and interpretability dashboards

---

## Repository

[https://github.com/Beemnet/fx-prediction.git](https://github.com/Beemnet/fx-prediction.git)

---
