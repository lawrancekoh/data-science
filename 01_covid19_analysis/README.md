# COVID-19 Global Impact Analysis

## 📌 Overview
This project provides a comprehensive analysis of the COVID-19 pandemic using the "Our World in Data" dataset. It explores global trends, regional disparities, and the effectiveness of various metrics such as fatality rates and infection growth. The goal is to derive actionable insights into how the pandemic evolved over time across different continents and countries.

## 🎯 Problem Statement
The COVID-19 pandemic generated vast amounts of data. Understanding this data is crucial for policymakers and health organizations to make informed decisions. This project aims to:
- Identify global and regional trends in cases and deaths.
- Analyze the correlation between different health metrics (e.g., cases vs. deaths).
- Visualize the spread and impact of the virus over time.

## 🛠 Tools & Tech Stack
- **Python**: Core programming language for data analysis.
- **Pandas**: Used for data manipulation, cleaning (handling missing values >90%), and aggregation.
- **Matplotlib & Seaborn**: Employed for static visualizations including multi-axis plots, box plots, and bar charts.
- **Plotly**: Used for interactive visualizations to allow users to explore data dynamically.
- **Data Domain**: Epidemiology (Cases, Deaths, Fatality Rates), Time Series Analysis.

## 📊 Methodology
1. **Data Cleaning**:
   - Dropped columns with >90% missing data to focus on reliable metrics.
   - Imputed missing values for key indicators using statistical measures (mean/median).
2. **Exploratory Data Analysis (EDA)**:
   - **Trend Analysis**: Plotted global daily cases and deaths over time.
   - **Regional Analysis**: Compared total cases and deaths across continents using bar charts.
   - **Distribution Analysis**: Used box plots to understand the spread of cases/deaths yearly.
3. **Advanced Visualization**:
   - Created multi-axis plots to overlay new cases vs. new deaths to see lag effects.
   - Developed interactive charts for user-driven exploration.

## 🔑 Key Insights
- **Fatality Trends**: Analyzed how the Case Fatality Rate (CFR) changed over the course of the pandemic.
- **Regional Hotspots**: Identified which continents bore the brunt of new waves at different times.
- **Data Quality**: Highlighted the challenge of missing data in global health datasets and implemented robust handling strategies.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Navigate to the notebooks directory:
   ```bash
   cd notebooks
   ```
3. Open and run the notebook:
   ```bash
   jupyter notebook "01_covid19_global_analysis.ipynb"
   ```
