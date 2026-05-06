# Fake News Detection

## 📌 Overview
Multi-model NLP pipeline for classifying news articles as real or fake. Compares Logistic Regression, Naive Bayes, Random Forest, and Gradient Boosting classifiers on TF-IDF text features, then combines them via a StackingClassifier for improved performance.

## 🎯 Problem Statement
"Fake news" causes confusion and can manipulate public opinion. Automating the detection of deceptive content is essential for social media and news platforms. This project aims to classify news items as "Real" or "Fake" based on their textual content, providing a robust solution for misinformation detection.

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| Fake and Real News Dataset | News articles labeled as real or fake from various sources | 44,898 articles | CSV | 2023-06-10 |

### Data Acquisition
Dataset compiled from multiple sources including:
- Fake News Detection on Kaggle (5,182 real, 5,182 fake)
- BS Detector GitHub repository
- Various news sources and fact-checking websites

The dataset contains columns for article text, title, and labels indicating real/fake status.

## 🔧 Preprocessing & Data Cleaning
### Data Quality Issues Identified
- **Missing values**: Some articles with missing text or labels
- **Text quality**: HTML tags, special characters, inconsistent formatting
- **Class imbalance**: Slight imbalance between real and fake classes
- **Duplicate articles**: Multiple entries for same news story
- **Text length variation**: Articles ranging from 50 to 5000+ words

### Cleaning Steps Applied
1. **Missing value handling**: Removed rows with missing text or labels
2. **Text cleaning**:
   - Removed HTML tags and special characters
   - Standardized text formatting
   - Removed extra whitespace and line breaks
3. **Duplicate detection**: Used text similarity to identify and remove duplicates
4. **Text normalization**: Converted all text to lowercase
5. **Data splitting**: Created train/test splits with stratification

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, Pandas 2.0, NumPy 1.24 |
| NLP | NLTK 3.8, spaCy 3.5, TextBlob 0.17 |
| Machine Learning | Scikit-learn 1.3, SciPy 1.10 |
| Visualization | Matplotlib 3.7, Seaborn 0.12 |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### Text Preprocessing Pipeline
1. **Text cleaning**: Removal of HTML tags, special characters, and stopwords
2. **Tokenization**: Word-level tokenization using NLTK
3. **Lemmatization**: Using spaCy for morphological analysis
4. **Vectorization**: TF-IDF transformation with N-gram features

### Feature Engineering
- **TF-IDF vectors**: Unigrams, bigrams, and trigrams (1-3 grams)
- **Text statistics**: Word count, character count, sentence count
- **Linguistic features**: POS tag frequencies, readability scores
- **Sentiment features**: TextBlob sentiment polarity and subjectivity

### Model Development
#### Base Models
- **Logistic Regression**: Linear model with L2 regularization
- **Naive Bayes**: MultinomialNB with Laplace smoothing
- **Random Forest**: Ensemble of 100 decision trees
- **Gradient Boosting**: XGBoost implementation with early stopping

#### Ensemble Approach
- **Stacking Classifier**: Meta-learner combining base model predictions
- **Blending**: Train meta-learner on predictions from hold-out set
- **Cross-validation**: 5-fold CV for robust performance estimation

## 📈 Model Performance Metrics
### Evaluation Results
| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.912 | 0.915 | 0.908 | 0.911 | 0.947 |
| Naive Bayes | 0.885 | 0.889 | 0.880 | 0.884 | 0.921 |
| Random Forest | 0.931 | 0.933 | 0.929 | 0.931 | 0.961 |
| Gradient Boosting | 0.942 | 0.945 | 0.940 | 0.942 | 0.972 |
| Stacking Ensemble | 0.948 | 0.950 | 0.946 | 0.948 | 0.976 |

### Performance Analysis
- **Confusion Matrix**: Detailed breakdown of true/false positives/negatives
- **ROC Curves**: Visual comparison of model discrimination ability
- **Precision-Recall Curves**: Analysis of trade-offs for imbalanced data
- **Feature Importance**: TF-IDF feature weights and model-specific importance

## 🔑 Key Findings & Business Insights
### Technical Insights
- **Ensemble superiority**: Stacking improved accuracy by 0.6-1.6% over individual models
- **Feature importance**: TF-IDF unigrams and bigrams were most informative
- **Class separation**: Fake news tended to use more emotive and sensationalist language
- **Model robustness**: Gradient Boosting showed best balance of precision and recall

### Business Value
- **Misinformation mitigation**: Automated detection reduces manual fact-checking burden
- **Real-time monitoring**: Model can be deployed for social media monitoring
- **Scalability**: Pipeline can handle large volumes of news articles
- **Accuracy trade-offs**: High precision reduces false positives in detection

## 🚀 How to Run
### Setup
```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies with pinned versions
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### Execution
```bash
# Navigate to project
cd 06_fake_news_detection

# Launch Jupyter Notebook
jupyter notebook notebooks/06_fake_news_detection.ipynb
```

## 📁 Project Structure
```
06_fake_news_detection/
├── data/           # News articles dataset (CSV)
├── notebooks/      # Full analysis and modeling notebook
├── results/        # Performance metrics and visualizations
├── models/         # Trained model files (pickle)
└── README.md       # Project documentation
```

## 📝 Dependencies
- Python 3.8+
- pandas==2.0.3
- numpy==1.24.3
- scikit-learn==1.3.0
- scipy==1.10.1
- matplotlib==3.7.1
- seaborn==0.12.2
- nltk==3.8.1
- spacy==3.5.3
- textblob==0.17.1

## 📚 References
- Fake News Detection on Kaggle: https://www.kaggle.com/datasets
- BS Detector GitHub Repository
- "Liar, Liar Pants on Fire": A New Benchmark Dataset for Fake News Detection
- Automated Fake News Detection Using Ensemble Learning Techniques

## 🤝 License
MIT — See LICENSE file for details.
