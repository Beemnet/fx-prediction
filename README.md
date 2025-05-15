# FMP Project

## Overview

The FMP project is to predict market trends for the exchange rate between the dollar and euros. This involves both classification (predicting directional movement) and regression (predicting the next exchange rate value). The project's goal is to leverage **dummy** financial data and advanced machine learning techniques to build accurate and insightful predictive models.

## Project Structure

```
fmp/
|
├── data/
│   ├── raw/                      # Raw dummy data (original datasets)
│   ├── processed/                # Cleaned and preprocessed datasets
│   └── external/                 # Additional datasets (e.g., external economic indicators)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb # EDA and initial insights
│   ├── 02_data_preprocessing.ipynb # Data cleaning and feature engineering
│   ├── 03_model_training.ipynb   # Training initial models
│   ├── 04_model_evaluation.ipynb # Model evaluation and comparison
│   └── 05_deployment_demo.ipynb  # Prototype or deployment testing
│
├── scripts/
│   │
│   ├── modelling/
│   │   ├── clean.py          # TODO: Data cleaning and formatting
│   │   ├── inference.py      # TODO: Inference pipeline
│   │   ├── preprocess.py     # TODO: Preprocessing steps (e.g., normalization, encoding)
│   │   ├── train.py          # TODO: Model training and saving
│   │
│   ├── scraping/
│   │   ├── alpha_vantage.py              # COMPLETE: Fetch and store USD/EUR exchange rate using Alpha Vantage
│   │   ├── bingnews_fetch.py             # TODO: Query Bing News API
│   │   ├── contextualweb_fetch.py        # COMPLETE: Contains modular functions for multiple RapidAPI sources
│   │   ├── ecb_rss_fetch.py              # TODO: Parse and store ECB RSS feed data
│   │   ├── google_news_rss_fetch.py      # TODO: Parse and store Google News RSS feed data
│   │   ├── news_api.py                   # COMPLETE: Query Real-Time News API and store JSON results
│   │   ├── run_contextual.py             # COMPLETE: Calls `contextualweb_fetch` functions with saved JSON dumps
│   │   ├── yahoo_finance.py              # COMPLETE: Collect and store USD/EUR data using yfinance in multiple granularities
│   │
│   ├── .env                     # Local environment variables
│   ├── requirements.txt         # COMPLETE: Python package dependencies
│
├── models/
│   ├── saved_models/             # Serialized models (e.g., .pkl or .h5 files)
│   └── experiments/              # Logs and artifacts for different model experiments
│
├── config/
│   ├── config.yaml               # Configuration file for parameters (e.g., paths, hyperparameters)
│   └── logging.yaml              # Logging configuration
│
├── tests/
│   ├── test_data_processing.py   # Unit tests for data processing
│   ├── test_model_training.py    # Unit tests for model training
│   └── test_end_to_end.py        # End-to-end pipeline tests
│
├── reports/
│   ├── figures/                  # Plots and graphs for reports
│   └── final_report.pdf          # Final project report
│
├── requirements.txt              # List of Python dependencies
├── README.md                     # Overview of the project
├── main.py                       # Main script to run the pipeline
├── LICENSE                       # License file for the project
└── .gitignore                    # Files and folders to ignore in version control

```

## Description of the scraping scripts (5/8 Complete)

### Scraping Script Descriptions

1. **`alpha_vantage.py`** – Fetches the current USD to EUR exchange rate, bid and ask prices using the Alpha Vantage API.

2. **`bingnews_fetch.py`** – Queries Bing News Search for articles related to currency or economic topics. _(TODO)_

3. **`contextualweb_fetch.py`** – Defines reusable functions for various financial and news-related data requests via RapidAPI (used by `run_contextual.py`).

**Requests handled by `contextualweb_fetch.py` (via RapidAPI):**

- **Real-Time Finance Data** – Retrieves historical cash flow statements for public companies.
- **Google News (v13 & v22)** – Searches and retrieves articles using two different versions of Google News API, currently searching r.
- **Reuters News** – Attempts to fetch global financial headlines and details (not usable unless subscribed).
- **Forex Factory Events** – Gets macroeconomic calendar events with timestamps, currencies, and market impact levels.
- **Real-Time News Data** –

  - `/search`: Searches news articles by keyword (e.g., "tariff").
  - `/topic-headlines`: Fetches top headlines for a specific topic (e.g., WORLD).
  - `/full-story-coverage`: Retrieves all coverage related to a particular story ID.

5. **`ecb_rss_fetch.py`** – Extracts and parses latest announcements and updates from the European Central Bank RSS feed. _(TODO)_

6. **`google_news_rss_fetch.py`** – Parses the Google News RSS feed for USD/EUR or macroeconomic developments. _(TODO)_

7. **`news_api.py`** – Queries and stores recent news articles using the Real-Time News Data API from RapidAPI.

8. **`run_contextual.py`** – Calls specific functions from `contextualweb_fetch.py` to perform the above RapidAPI requests and store each response in JSON.

9. **`yahoo_finance.py`** – Downloads historical USD/EUR exchange rate data in multiple granularities (1m, 2m, 5m, 30m, 60m, 1d) using Yahoo Finance and saves them as CSVs.

## Using web scraping scripts:

**1. Navigate to the scripts/scraping folder:**

```bash
cd ./scripts/scraping
```

**2. Run the complete scraping files as you need:**

1. Real-Time News API

```bash
python news_api.py
```

2. Alpha Vantage exchange rate fetch

```bash
python alpha_vantage.py
```

3. Yahoo Finance historical exchange rate fetch

```bash
python yahoo_finance.py
```

4. Run contextual API requests and store responses

```bash
python run_contextual.py
```


## Tasks

### 1. **Define the Objective** [DONE-ish]

**Goal**: Predict market trends for the exchange rate between the dollar and euros. <br>

**Key Outputs**:

- Predict whether the rate will go up, down, or stay flat (classification).
- Predict the next rate value (regression).
- Evaluation Metrics: Accuracy, RMSE (Root Mean Square Error), MAPE (Mean Absolute Percentage Error), etc.

### 2. **Data Collection and Preparation** [DOING]

**Data Description:**
- Exchange rate data (dummy data for now).
- Additional data (if applicable): interest rates, inflation rates, economic indicators, or financial news sentiment.<br>

**Steps:**
  * Load and explore data (check for completeness, trends, and outliers). [DOING]
  * Handle missing data (imputation or removal).
  * Perform feature engineering (e.g., moving averages, volatility, or lag features). [DOING]

### 3. **Exploratory Data Analysis (EDA)** [DOING]

**Visualizations:**

- Time series plot of exchange rates.
- Correlation analysis of features.
- Trend and seasonality analysis.<br>

**Statistical Insights:**

- Distribution of exchange rates.
- Identify anomalies or structural breaks.

### 4. **Model Selection**

**Baseline Models:**

- Naive forecasting (e.g., last known value).
- Linear Regression.<br>

**Advanced Models:**

- ARIMA or SARIMA for time series forecasting.
- Machine Learning models: Random Forest, Gradient Boosting (e.g., XGBoost, LightGBM), or Neural Networks.
- Deep Learning models: LSTMs or Transformers for time series.

### 5. Model Training and Validation

**Data Split**:

- Train/test split (e.g., 80%/20%).
- Consider time series cross-validation.<br>

**Hyperparameter Tuning:**

- Use Grid Search or Bayesian Optimization to optimize model parameters.

### 6. Model Evaluation

**Use appropriate metrics:**

- Regression: RMSE, MAPE.
- Classification: Accuracy, Precision, Recall, F1-Score.<br>
  Compare models against the baseline.

### 8. Deployment Plan

- Build a prototype for real-time predictions.
- Use tools like Flask or FastAPI for a backend API.
- Consider visualization dashboards for live monitoring (e.g., Dash or Power BI).

### 9. Documentation and Reporting

- Summarize methodology, results, and insights.
- Highlight potential business implications of the model predictions.

## Getting Started

Clone the repository and navigate to the project folder:

```

git clone https://github.com/personal_forex/fmp.git
cd fmp

```

### Install dependencies:

```

pip install -r requirements.txt

```

Run the main pipeline:

```

python main.py

```

## Contribution

Fork the repository or submit a pull request.

## License

Permission to access, use, or modify this software is strictly limited to authorized individuals who have received prior written consent from personal_forex. Any unauthorized access, use, modification, or distribution is strictly prohibited and subject to legal action.
```
