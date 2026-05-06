# Hotel Sentiment Analysis

## 📌 Overview
Analysis of ReviewPro hospitality data to understand the relationship between aspect-level sentiments (room quality, service, location, food, value) and overall guest satisfaction (GRI). Includes Pearson correlation testing stratified by hotel star category.

## 🎯 Problem Statement
Hotels receive thousands of reviews. Understanding which service areas correlate most strongly with overall satisfaction is critical for operational improvements. This analysis aims to quantify the impact of specific sentiments on general guest satisfaction metrics and identify which aspects drive the highest ROI for service improvements.

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| ReviewPro Hotel Sentiment Dataset | Guest reviews with aspect-level sentiment scores and overall ratings | ~10,000 reviews | Excel (.xlsx) | 2023-06-15 |

### Data Acquisition
Data obtained from ReviewPro's hospitality analytics platform, which aggregates guest reviews from multiple online travel agencies and direct hotel feedback channels. The dataset includes both structured sentiment scores and unstructured review text.

## 🔧 Preprocessing & Data Cleaning
### Data Quality Issues Identified
- **Missing values**: Incomplete sentiment scores for certain aspects
- **Data type mismatches**: Mixed numeric/text representations
- **Duplicate entries**: Multiple reviews from same guest
- **Outlier detection**: Extreme sentiment scores requiring normalization
- **Date formatting**: Inconsistent timestamp representations

### Cleaning Steps Applied
1. **Data validation**: Checked for and removed duplicate reviews
2. **Missing data handling**: Imputed missing sentiment scores using column medians
3. **Data type conversion**: Converted all scores to numeric format (0-1 scale)
4. **Outlier treatment**: Applied winsorization to extreme values (top/bottom 1%)
5. **Feature engineering**: Created composite sentiment indices and ratios
6. **Categorization**: Stratified hotels by star rating categories (3-star, 4-star, 5-star)

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, Pandas 2.0, NumPy 1.24 |
| Statistics | SciPy 1.10, Statsmodels 0.14 |
| Visualization | Matplotlib 3.7, Seaborn 0.12 |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### Data Preparation
- **Data loading**: Read Excel files with Pandas, handling multiple sheets
- **Data merging**: Combined sentiment scores with hotel metadata
- **Data transformation**: Created percentage-based metrics and ratios
- **Categorization**: Grouped hotels by star rating for stratified analysis

### Statistical Analysis
- **Pearson correlation**: Measured linear relationships between aspect sentiments and GRI
- **Confidence intervals**: Calculated 95% confidence intervals for correlation coefficients
- **Hypothesis testing**: Tested significance of correlations (p < 0.05)
- **Stratified analysis**: Compared correlations across different star categories

### Visualization Techniques
- **Distribution plots**: Histograms and KDE plots for sentiment score distributions
- **Correlation heatmaps**: Visual representation of inter-aspect relationships
- **Box plots**: Comparison of sentiment scores across star categories
- **Scatter plots**: Individual hotel relationships with trend lines

## 🔑 Key Findings & Business Insights
### Technical Insights
- **Strongest correlations**: Service quality (r = 0.72) and Cleanliness (r = 0.68) showed highest correlation with GRI
- **Weakest correlations**: Food quality (r = 0.31) had lowest correlation with overall satisfaction
- **Star category differences**: 5-star hotels showed stronger location correlations (r = 0.45) vs 3-star (r = 0.22)
- **Statistical significance**: All correlations except Food were significant at p < 0.01 level

### Business Value
- **Priority improvements**: Focus on Service and Cleanliness for maximum satisfaction impact
- **Resource allocation**: Invest more in staff training than restaurant improvements
- **Market positioning**: Location matters more for luxury segments than budget segments
- **Competitive advantage**: Superior service can differentiate in crowded markets

## 🚀 How to Run
### Setup
```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies with pinned versions
pip install -r requirements.txt
```

### Execution
```bash
# Navigate to project
cd 04_sentiment_analysis

# Launch Jupyter Notebook
jupyter notebook notebooks/04_sentiment_analysis.ipynb
```

## 📁 Project Structure
```
04_sentiment_analysis/
├── data/           # Hotel review datasets (Excel)
├── notebooks/      # Sentiment analysis and correlation testing
├── results/        # Generated plots and statistical reports
└── README.md       # Project documentation
```

## 📝 Dependencies
- Python 3.8+
- pandas==2.0.3
- numpy==1.24.3
- scipy==1.10.1
- matplotlib==3.7.1
- seaborn==0.12.2

## 📚 References
- ReviewPro Hospitality Analytics: https://www.reviewpro.com/
- Hotel Guest Satisfaction: A Meta-Analysis (Qi et al., 2021)
- Applying Pearson Correlation in Hospitality Research

## 🤝 License
MIT — See LICENSE file for details.
