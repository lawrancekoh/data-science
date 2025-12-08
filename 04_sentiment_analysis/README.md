# Hotel Sentiment Analysis

## 📌 Overview
This project delves into guest sentiment analysis for the hospitality industry. By analyzing hotel reviews and correlating them with ratings (GRI - Global Review Index), it uncovers which specific aspects of a hotel (Cleanliness, Service, Location, etc.) drive positive or negative guest satisfaction.

## 🎯 Problem Statement
Hotels receive thousands of reviews. Understanding which service areas correlate most strongly with overall satisfaction is critical for operational improvements. This analysis aims to quantify the impact of specific sentiments on general guest satisfaction metrics.

## 🛠 Tools & Tech Stack
- **Python**: Core language.
- **Pandas**: extensively used for handling structured review data and Excel files.
- **SciPy**: For probability distributions and statistical functions.
- **Seaborn & Matplotlib**: For statistical data visualization.
- **Domain Focus**: Market Research, Customer Sentiment, Correlation Analysis.

## 📊 Methodology
1. **Data Acquisition**:
   - Loading review data including "GRI" (Global Review Index) and aspect-specific mentions (Room, Service, Food, etc.) from Excel.
2. **Data Cleaning & Structure**:
   - Transforming raw counts of positive/negative mentions into usable metrics.
   - Merging sentiment data with star ratings for category-based analysis.
3. **Statistical Analysis**:
   - **Confidence Intervals**: Calculating mean confidence intervals for different metrics.
   - **Correlation**: Using Pearson correlation to measure the strength of relationships between specific attributes (e.g., "Cleanliness_pos") and overall GRI.
4. **Visualization**:
   - Visualizing the distribution of sentiments across different star categories (3-star vs. 5-star hotels).

## 🔑 Key Insights
- **Service & Cleanliness**: Typically show the strongest correlation with overall guest satisfaction scores.
- **Star Category Impact**: Expectations and sentiment drivers vary significantly between 3-star and 5-star properties.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Navigate to the notebooks directory:
   ```bash
   cd notebooks
   ```
3. Open the analysis notebook:
   ```bash
   jupyter notebook "04_sentiment_analysis.ipynb"
   ```
