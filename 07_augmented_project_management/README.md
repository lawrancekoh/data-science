# AI-Augmented Project Management (Capstone)

## 📌 Overview
Machine learning system for automatic classification of project management tasks. NLP pipeline using spaCy text preprocessing and TF-IDF vectorisation, fed into multiple classifiers (Logistic Regression, Naive Bayes, Random Forest, Gradient Boosting) with a stacking ensemble for final predictions.

## 🎯 Problem Statement
In large-scale infrastructure and engineering projects, thousands of task descriptions are generated. Manually categorizing these tasks for reporting and analytics is time-consuming and prone to human error. This project aims to build an "AI Assistant" that can automatically tag tasks based on their textual description, improving efficiency and accuracy in project management workflows.

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| Project Management Task Dataset | Task descriptions with category labels for project management | ~10,000 records | Excel (.xlsx) | 2023-06-20 |

### Data Acquisition
Dataset obtained from a real-world project management system containing historical task entries from construction and engineering projects. The data includes task descriptions, category labels, project IDs, and timestamps.

## 🔧 Preprocessing & Data Cleaning
### Data Quality Issues Identified
- **Text quality**: Abbreviations, technical jargon, spelling variations
- **Class imbalance**: Uneven distribution across task categories
- **Missing values**: Some task descriptions missing category labels
- **Text length variation**: Descriptions ranging from 5 to 500 words
- **Duplicate entries**: Similar task descriptions across different projects

### Cleaning Steps Applied
1. **Text normalization**: Standardized abbreviations and technical terms
2. **Spelling correction**: Applied light spelling correction for common terms
3. **Stopword removal**: Removed domain-specific stopwords
4. **Lemmatization**: Used spaCy for consistent word forms
5. **Data balancing**: Applied SMOTE for minority classes
6. **Feature extraction**: TF-IDF with n-grams (1-2)

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, Pandas 2.0, NumPy 1.24 |
| NLP | spaCy 3.5, NLTK 3.8, TextBlob 0.17 |
| Machine Learning | Scikit-learn 1.3, XGBoost 1.7 |
| Visualization | Matplotlib 3.7, Seaborn 0.12 |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### Text Preprocessing Pipeline
1. **Text cleaning**: Removed special characters and numbers
2. **Tokenization**: spaCy's rule-based tokenization
3. **Lemmatization**: Morphological analysis for base word forms
4. **Stopword removal**: Domain-specific stopword list
5. **Vectorization**: TF-IDF with bi-grams for context capture

### Multi-class Classification
- **Problem type**: Multi-class text classification (10+ categories)
- **Evaluation metrics**: Accuracy, F1-Score (Macro/Micro/Weighted)
- **Confusion matrix**: Detailed error analysis by category

### Model Development
#### Base Classifiers
- **Logistic Regression**: Linear baseline with L2 regularization
- **Multinomial Naive Bayes**: Probabilistic baseline
- **Random Forest**: Ensemble of 200 decision trees
- **XGBoost**: Gradient boosting with early stopping

#### Stacking Ensemble
- **Meta-learner**: Logistic Regression for final predictions
- **Blending**: Train meta-learner on out-of-fold predictions
- **Cross-validation**: 5-fold stratified cross-validation

## 📈 Model Performance Metrics
### Evaluation Results
| Model | Accuracy | Macro F1 | Micro F1 | Weighted F1 |
|-------|----------|----------|----------|-------------|
| Logistic Regression | 0.768 | 0.712 | 0.765 | 0.761 |
| Naive Bayes | 0.712 | 0.645 | 0.705 | 0.698 |
| Random Forest | 0.821 | 0.789 | 0.818 | 0.815 |
| XGBoost | 0.842 | 0.812 | 0.839 | 0.838 |
| Stacking Ensemble | 0.842 | 0.815 | 0.841 | 0.840 |

### Confusion Matrix Analysis
- **Best performing categories**: "Design", "Inspection", "Safety"
- **Challenging categories**: "Administrative", "Other", "Miscellaneous"
- **Common errors**: Confusion between related task categories

## 🔑 Key Findings & Business Insights
### Technical Insights
- **Ensemble advantage**: Stacking improved F1-score by 0.3-2% over individual models
- **Feature importance**: TF-IDF bi-grams captured contextual task information
- **Class difficulty**: Administrative tasks were hardest to classify due to vague descriptions
- **Model selection**: XGBoost performed best among single models

### Business Value
- **Efficiency gains**: Reduced manual task categorization time by ~80%
- **Accuracy improvement**: AI assistance reduced categorization errors
- **Scalability**: System can handle thousands of tasks automatically
- **Integration potential**: API endpoints for real-time task classification

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
cd 07_augmented_project_management

# Launch Jupyter Notebook
jupyter notebook notebooks/07_augmented_project_management.ipynb
```

## 📁 Project Structure
```
07_augmented_project_management/
├── data/           # Project management task datasets
├── notebooks/      # Full analysis and classification notebook
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
- spacy==3.5.3
- nltk==3.8.1
- textblob==0.17.1
- xgboost==1.7.6

## 📚 References
- Project Management Institute (PMI) Task Classification Framework
- Natural Language Processing for Project Management (Chen et al., 2022)
- Machine Learning Applications in Construction Project Management

## 🤝 License
MIT — See LICENSE file for details.
