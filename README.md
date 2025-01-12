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
│   ├── data_preprocessing.py     # Scripts for cleaning and processing data
│   ├── feature_engineering.py    # Scripts for feature creation
│   ├── train_model.py            # Training and saving models
│   ├── evaluate_model.py         # Evaluation and metrics calculation
│   ├── predict.py                # Script for making predictions
│   └── utils.py                  # Utility functions (e.g., file handling, plotting)
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


## Tasks

### 1. **Define the Objective**

**Goal**: Predict market trends for the exchange rate between the dollar and euros. <br>

**Key Outputs**:
  * Predict whether the rate will go up, down, or stay flat (classification).
  * Predict the next rate value (regression).
  * Evaluation Metrics: Accuracy, RMSE (Root Mean Square Error), MAPE (Mean Absolute Percentage Error), etc.

### 2. **Data Collection and Preparation**

**Data Description:**
  * Exchange rate data (dummy data for now).
  * Additional data (if applicable): interest rates, inflation rates, economic indicators, or financial news sentiment.<br>

**Steps:**
  * Load and explore data (check for completeness, trends, and outliers).
  * Handle missing data (imputation or removal).
  * Perform feature engineering (e.g., moving averages, volatility, or lag features).

### 3. **Exploratory Data Analysis (EDA)**

**Visualizations:**
  * Time series plot of exchange rates.
  * Correlation analysis of features.
  * Trend and seasonality analysis.<br>

**Statistical Insights:**
  * Distribution of exchange rates.
  * Identify anomalies or structural breaks.

### 4. **Model Selection**

**Baseline Models:**
  * Naive forecasting (e.g., last known value).
  * Linear Regression.<br>

**Advanced Models:**
  * ARIMA or SARIMA for time series forecasting.
  * Machine Learning models: Random Forest, Gradient Boosting (e.g., XGBoost, LightGBM), or Neural Networks.
  * Deep Learning models: LSTMs or Transformers for time series.

### 5. Model Training and Validation

**Data Split**:
  * Train/test split (e.g., 80%/20%).
  * Consider time series cross-validation.<br>

**Hyperparameter Tuning:**
  * Use Grid Search or Bayesian Optimization to optimize model parameters.

### 6. Model Evaluation

**Use appropriate metrics:**
  * Regression: RMSE, MAPE.
  * Classification: Accuracy, Precision, Recall, F1-Score.<br>
Compare models against the baseline.

### 8. Deployment Plan

  * Build a prototype for real-time predictions.
  * Use tools like Flask or FastAPI for a backend API.
  * Consider visualization dashboards for live monitoring (e.g., Dash or Power BI).

### 9. Documentation and Reporting

  * Summarize methodology, results, and insights.
  * Highlight potential business implications of the model predictions.


## Getting Started 

Clone the repository and navigate to the project folder:
```
git clone https://github.com/Beemnet/fmp.git
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

Fork the repository.

Create a feature branch.

Commit your changes.

Submit a pull request.

## License

Permission to access, use, or modify this software is strictly limited to authorized individuals who have received prior written consent from [Your Name or Organization Name]. Any unauthorized access, use, modification, or distribution is strictly prohibited and subject to legal action.

