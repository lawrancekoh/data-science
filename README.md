# Data Science Portfolio

> A curated collection of data science projects spanning exploratory analysis, NLP, machine learning, and customer analytics — each demonstrating production-quality methodologies and business-relevant insights.

## Overview

This repository showcases data science expertise across seven end-to-end projects, ranging from **pandemic trend analysis** and **passenger survival modelling** to **fake news detection**, **customer segmentation**, and **automated project management systems**. Each project demonstrates proficiency in the full data science workflow: data ingestion, cleaning, feature engineering, statistical analysis, machine learning modelling, and actionable business insights.

## Projects

### 1. COVID-19 Global Impact Analysis
Comprehensive time-series analysis of the COVID-19 pandemic using the "Our World in Data" dataset. Covers daily case/death trends, fatality rate analysis, vaccination rollout patterns, testing effectiveness, and regional comparisons across continents and individual countries.

**Techniques:** Time-series aggregation, rolling averages, fatality rate modelling, cross-country comparisons, interactive exploration.  
**Stack:** pandas, matplotlib, seaborn

📓 [Notebook →](./01_covid19_analysis/notebooks/01_covid19_global_analysis.ipynb)

### 2. Titanic Survival Analysis
Complete exploratory data analysis and predictive modelling on the classic Titanic dataset. Examines how socioeconomic class, gender, age, and family size influenced survival outcomes — with data cleaning, feature engineering, and statistical inference.

- **02-1**: Statistical analysis with data cleaning (median/mode imputation), feature engineering (FamilySize, AgeGroup), and survival rate analysis across demographics
- **02-2**: Visual analysis with distribution plots, correlation heatmaps, and categorical comparisons

**Techniques:** Missing value imputation, feature engineering, groupby analysis, statistical visualisations  
**Stack:** pandas, numpy, matplotlib, seaborn

📓 [Analysis →](./02_titanic_analysis/notebooks/02-1_titanic_survival_analysis.ipynb) · 📓 [Visualisations →](./02_titanic_analysis/notebooks/02-2_titanic_visualisations.ipynb)

### 3. Extractive Text Summarisation
Frequency-based NLP pipeline that automatically generates summaries from domain-specific articles. Uses NLTK for sentence tokenisation, word frequency scoring, and threshold-based sentence selection to produce concise summaries.

**Techniques:** NLP, tokenisation, stop-word filtering, frequency-based sentence scoring  
**Stack:** NLTK

📓 [Notebook →](./03_text_summarization/notebooks/03_text_summarization.ipynb)

### 4. Hotel Sentiment Analysis
Analysis of ReviewPro hospitality data to understand the relationship between aspect-level sentiments (room quality, service, location, food, value) and overall guest satisfaction (GRI). Includes Pearson correlation testing stratified by hotel star category.

**Techniques:** Correlation analysis, Pearson significance testing, stratified groupby analysis  
**Stack:** pandas, numpy, scipy, matplotlib, seaborn

📓 [Notebook →](./04_sentiment_analysis/notebooks/04_sentiment_analysis.ipynb)

### 5. Customer Segmentation via RFM
Recency-Frequency-Monetary (RFM) analysis to segment a customer base from transaction data. Computes RFM metrics per customer, applies quartile-based scoring, and classifies segments as "Most Valuable", "Loyal", or "Most Likely to Churn" for targeted marketing.

**Techniques:** RFM modelling, quantile-based scoring, aggregate profiling, distribution analysis  
**Stack:** pandas, numpy, matplotlib, seaborn

📓 [Notebook →](./05_customer_segmentation/notebooks/05_customer_segmentation.ipynb)

### 6. Fake News Detection
Multi-model NLP pipeline for classifying news articles as real or fake. Compares Logistic Regression, Naive Bayes, Random Forest, and Gradient Boosting classifiers on TF-IDF text features, then combines them via a StackingClassifier for improved performance.

**Techniques:** TF-IDF vectorisation, multi-model comparison, stacking ensembles, cross-validation, spaCy text preprocessing  
**Stack:** pandas, sklearn, scipy, spacy, matplotlib, seaborn

📓 [Notebook →](./06_fake_news_detection/notebooks/06_fake_news_detection.ipynb)
🗄️ [Draft noteboooks →](./_archive/)

### 7. AI-Augmented Project Management (Capstone)
Machine learning system for automatic classification of project management tasks. NLP pipeline using spaCy text preprocessing and TF-IDF vectorisation, fed into multiple classifiers (Logistic Regression, Naive Bayes, Random Forest, Gradient Boosting) with a stacking ensemble for final predictions.

**Techniques:** Multi-class text classification, stacking ensembles, lemmatisation, train-test validation  
**Stack:** pandas, sklearn, scipy, spacy, matplotlib, seaborn

📓 [Notebook →](./07_augmented_project_management/notebooks/07_augmented_project_management.ipynb)

## Technical Skills Demonstrated

### Languages & Tools
- **Python** — pandas, numpy, scipy, matplotlib, seaborn
- **Machine Learning** — scikit-learn (classification, ensembles, cross-validation, TF-IDF)
- **NLP** — NLTK (tokenisation, summarisation), spaCy (lemmatisation, preprocessing)
- **Statistical Analysis** — scipy.stats (Pearson correlation, significance testing)
- **Visualisation** — matplotlib, seaborn (distribution plots, heatmaps, categorical comparisons)

### Data Science Methodologies
| Category | Techniques |
|---|---|
| **Data Preprocessing** | Missing value imputation, duplicate removal, data type conversions, text cleaning |
| **Feature Engineering** | RFM computation, FamilySize, AgeGroup, date extraction, TF-IDF vectorisation |
| **Exploratory Analysis** | Distribution analysis, correlation matrices, groupby aggregations, outlier detection |
| **Machine Learning** | Logistic Regression, Naive Bayes, Random Forest, Gradient Boosting, StackingClassifier |
| **Model Evaluation** | Cross-validation, train-test splits, accuracy & F1 metrics, confusion matrices |
| **Statistical Inference** | Pearson correlation, significance testing, rate calculations |
| **NLP** | Sentiment analysis, extractive summarisation, tokenisation, lemmatisation, stop-word removal |

## Repository Structure

```
data-science/
├── 01_covid19_analysis/
│   ├── data/                     # Our World in Data COVID dataset
│   ├── notebooks/
│   │   └── 01_covid19_global_analysis.ipynb
│   └── README.md                 # Project-specific documentation
├── 02_titanic_analysis/
│   ├── data/                     # Titanic passenger dataset
│   └── notebooks/
│       ├── 02-1_titanic_survival_analysis.ipynb
│       └── 02-2_titanic_visualisations.ipynb
├── 03_text_summarization/
│   └── notebooks/03_text_summarization.ipynb
├── 04_sentiment_analysis/
│   ├── data/                     # ReviewPro hotel sentiment data
│   └── notebooks/04_sentiment_analysis.ipynb
├── 05_customer_segmentation/
│   ├── data/                     # Transaction data
│   └── notebooks/05_customer_segmentation.ipynb
├── 06_fake_news_detection/
│   └── notebooks/06_fake_news_detection.ipynb
├── 07_augmented_project_management/
│   ├── data/                     # Capstone project task data
│   ├── notebooks/
│   │   └── 07_augmented_project_management.ipynb
│   └── src/utils.py              # Shared utility functions
├── _archive/                     # Draft notebooks and presentation files
├── requirements.txt
├── README.md
└── LICENSE
```

## Setup

```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

## Contact

- **LinkedIn:** [Lawrance Koh](https://www.linkedin.com/in/lawrancekoh/)
- **Email:** lawrancekoh@outlook.com

## License

MIT — see [LICENSE](./LICENSE) for details.
