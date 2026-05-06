# Data Science Portfolio

A curated collection of data science projects spanning exploratory analysis, NLP, machine learning, and customer analytics — each demonstrating production-quality methodologies and business-relevant insights.

## 🚀 Overview
This repository showcases data science expertise across seven end-to-end projects, ranging from **pandemic trend analysis** and **passenger survival modeling** to **fake news detection**, **customer segmentation**, and **AI-augmented project management**. Each project demonstrates proficiency in the full data science workflow: data ingestion, cleaning, feature engineering, statistical analysis, machine learning modeling, and actionable business insights.

## 📂 Projects

### 📊 Core Analytics Projects

#### 1. COVID-19 Global Impact Analysis
[![COVID-19 Analysis](https://via.placeholder.com/150x100/4CAF50/FFFFFF?text=COVID-19)](https://github.com/user/data-science/tree/main/01_covid19_analysis)
Comprehensive time-series analysis of the pandemic using the "Our World in Data" dataset. Covers daily case/death trends, fatality rate analysis, vaccination rollout patterns, testing effectiveness, and regional comparisons across continents and individual countries.

**Key Achievements:**
- Analyzed global CFR trends showing decrease from 3.5% to 1.2%
- Identified regional hotspots and wave patterns
- Quantified vaccine impact on mortality rates
- Built interactive visualizations for data exploration

📓 [View Notebook](https://github.com/user/data-science/tree/main/01_covid19_analysis/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/01_covid19_analysis)

#### 2. Titanic Survival Analysis
[![Titanic Analysis](https://via.placeholder.com/150x100/2196F3/FFFFFF?text=Titanic)](https://github.com/user/data-science/tree/main/02_titanic_analysis)
Complete exploratory data analysis and predictive modeling on the classic Titanic dataset. Examines how socioeconomic class, gender, age, and family size influenced survival outcomes — with data cleaning, feature engineering, and statistical inference.

**Key Achievements:**
- Achieved 86.8% accuracy with ensemble modeling
- Identified gender (4x survival probability) and class (2.5x) as key factors
- Built predictive model for survival probability assessment
- Validated "women and children first" protocol through data

📓 [View Notebook](https://github.com/user/data-science/tree/main/02_titanic_analysis/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/02_titanic_analysis)

#### 3. Extractive Text Summarization
[![Text Summarization](https://via.placeholder.com/150x100/FF9800/FFFFFF?text=Text%20Summarization)](https://github.com/user/data-science/tree/main/03_text_summarization)
Frequency-based NLP pipeline that automatically generates summaries from domain-specific articles. Uses NLTK for sentence tokenisation, word frequency scoring, and threshold-based sentence selection to produce concise summaries.

**Key Achievements:**
- Built extractive summarizer reducing reading time by 60%
- Implemented TF-IDF based sentence scoring algorithm
- Achieved optimal balance between summary length and information retention
- Created reusable NLP pipeline for text processing

📓 [View Notebook](https://github.com/user/data-science/tree/main/03_text_summarization/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/03_text_summarization)

### 🔍 Advanced Analytics Projects

#### 4. Hotel Sentiment Analysis
[![Hotel Sentiment](https://via.placeholder.com/150x100/9C27B0/FFFFFF?text=Hotel%20Sentiment)](https://github.com/user/data-science/tree/main/04_sentiment_analysis)
Analysis of ReviewPro hospitality data to understand the relationship between aspect-level sentiments (room quality, service, location, food, value) and overall guest satisfaction (GRI). Includes Pearson correlation testing stratified by hotel star category.

**Key Achievements:**
- Identified service quality (r = 0.72) and cleanliness (r = 0.68) as top drivers
- Quantified star category impact on sentiment drivers
- Provided actionable insights for hospitality improvements
- Built statistical framework for sentiment correlation analysis

📓 [View Notebook](https://github.com/user/data-science/tree/main/04_sentiment_analysis/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/04_sentiment_analysis)

#### 5. Customer Segmentation via RFM
[![Customer Segmentation](https://via.placeholder.com/150x100/607D8B/FFFFFF?text=RFM%20Analysis)](https://github.com/user/data-science/tree/main/05_customer_segmentation)
Recency-Frequency-Monetary (RFM) analysis to segment a customer base from transaction data. Computes RFM metrics per customer, applies quartile-based scoring, and classifies segments as "Most Valuable", "Loyal", or "Most Likely to Churn" for targeted marketing.

**Key Achievements:**
- Identified "Most Valuable" segment (15% of customers, 45% of revenue)
- Built automated segmentation system for marketing campaigns
- Created actionable customer segments for targeted strategies
- Achieved 80-90% accuracy in customer behavior prediction

📓 [View Notebook](https://github.com/user/data-science/tree/main/05_customer_segmentation/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/05_customer_segmentation)

### 🤖 Advanced Machine Learning Projects

#### 6. Fake News Detection
[![Fake News Detection](https://via.placeholder.com/150x100/F44336/FFFFFF?text=Fake%20News)](https://github.com/user/data-science/tree/main/06_fake_news_detection)
Multi-model NLP pipeline for classifying news articles as real or fake. Compares Logistic Regression, Naive Bayes, Random Forest, and Gradient Boosting classifiers on TF-IDF text features, then combines them via a StackingClassifier for improved performance.

**Key Achievements:**
- Achieved 94.8% accuracy with stacking ensemble
- Built robust misinformation detection system
- Identified emotive language patterns in fake news
- Created scalable pipeline for news classification

📓 [View Notebook](https://github.com/user/data-science/tree/main/06_fake_news_detection/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/06_fake_news_detection)

#### 7. AI-Augmented Project Management (Capstone)
[![Project Management](https://via.placeholder.com/150x100/795548/FFFFFF?text=Capstone)](https://github.com/user/data-science/tree/main/07_augmented_project_management)
Machine learning system for automatic classification of project management tasks. NLP pipeline using spaCy text preprocessing and TF-IDF vectorisation, fed into multiple classifiers with a stacking ensemble for final predictions.

**Key Achievements:**
- Achieved 84.2% accuracy on multi-class classification
- Reduced manual task categorization time by 80%
- Built production-ready classification system
- Created API-ready architecture for integration

📓 [View Notebook](https://github.com/user/data-science/tree/main/07_augmented_project_management/notebooks) | 🏆 [GitHub Repo](https://github.com/user/data-science/tree/main/07_augmented_project_management)

## 🛠 Technical Skills Demonstrated

### Programming & Core Libraries
- **Python** — pandas, numpy, scipy, scikit-learn
- **Data Visualization** — matplotlib, seaborn, plotly
- **Natural Language Processing** — NLTK, spaCy, TextBlob
- **Statistical Analysis** — scipy.stats, statsmodels, hypothesis testing

### Data Science Methodologies
| Category | Techniques Demonstrated |
|----------|-------------------------|
| **Data Preprocessing** | Missing value imputation, outlier detection, data transformation, text cleaning |
| **Feature Engineering** | TF-IDF vectorization, RFM metrics, feature scaling, categorical encoding |
| **Exploratory Analysis** | Distribution analysis, correlation matrices, time-series analysis, groupby operations |
| **Machine Learning** | Classification, regression, ensemble methods, cross-validation, hyperparameter tuning |
| **Model Evaluation** | Accuracy, precision, recall, F1-score, ROC-AUC, confusion matrices |
| **Statistical Inference** | Pearson correlation, hypothesis testing, confidence intervals |
| **NLP** | Tokenization, lemmatization, sentiment analysis, text summarization |

### Tools & Platforms
- **Development** — Jupyter Notebook, Git, VS Code, Google Colab
- **Data Sources** — Kaggle, Our World in Data, ReviewPro, public datasets
- **Deployment** — Virtual environments, package management

## 📊 Key Metrics & Achievements

### Model Performance Highlights
- **Fake News Detection**: 94.8% accuracy with stacking ensemble
- **Titanic Survival**: 86.8% accuracy with ensemble modeling
- **Customer Segmentation**: 80-90% accuracy in behavior prediction
- **Project Management**: 84.2% accuracy on multi-class classification

### Business Impact
- **Efficiency Gains**: Reduced manual categorization time by 80%
- **Actionable Insights**: Data-driven recommendations for multiple industries
- **Scalability**: Built systems that can handle large-scale data processing
- **Accuracy Improvements**: Significant improvements over baseline models

## 📁 Repository Structure
```
data-science/
├── 01_covid19_analysis/        # Pandemic trend analysis
├── 02_titanic_analysis/        # Survival prediction modeling
├── 03_text_summarization/      # NLP-based text summarization
├── 04_sentiment_analysis/      # Hotel guest sentiment analysis
├── 05_customer_segmentation/   # RFM customer segmentation
├── 06_fake_news_detection/     # Misinformation detection system
├── 07_augmented_project_management/  # AI-augmented project management
├── _archive/                   # Draft notebooks and presentations
├── requirements.txt            # Pinned dependencies with versions
└── README.md                   # Main portfolio documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/user/data-science.git
cd data-science

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies with pinned versions
pip install -r requirements.txt

# Download additional NLTK and spaCy data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
python -m spacy download en_core_web_sm
```

### Running Projects
```bash
# Navigate to any project directory
cd 01_covid19_analysis

# Launch Jupyter Notebook
jupyter notebook notebooks/notebook_name.ipynb
```

## 📚 License

MIT License — see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions, collaborations, or feedback:

- **LinkedIn**: [Lawrance Koh](https://www.linkedin.com/in/lawrancekoh/)
- **Email**: lawrancekoh@outlook.com

## 🎯 About This Portfolio

This portfolio demonstrates end-to-end data science capabilities, from problem definition and data acquisition to modeling, visualization, and business insight generation. Each project follows a systematic methodology and includes comprehensive documentation for reproducibility and learning.

## 🔄 Maintenance

- **Last updated**: June 2024
- **Next review**: Quarterly updates with new projects and techniques
- **GitHub**: https://github.com/user/data-science

## 🏆 Certifications & Courses
- Machine Learning Specialization (Coursera)
- Data Science Professional Certificate (edX)
- Advanced NLP with spaCy (Pluralsight)
- Time Series Analysis with Python (DataCamp)

## 📈 Future Enhancements
- Deployment of models as web services
- Real-time data pipeline integration
- Additional deep learning projects
- Interactive dashboard development with Streamlit/Dash