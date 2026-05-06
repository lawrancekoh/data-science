# Titanic Survival Analysis

## 📌 Overview
Complete exploratory data analysis and predictive modeling on the classic Titanic dataset. Examines how socioeconomic class, gender, age, and family size influenced survival outcomes — with data cleaning, feature engineering, and statistical inference.

## 🎯 Problem Statement
The sinking of the Titanic is one of the most infamous shipwrecks in history. While there was some element of luck involved in surviving, it seems some groups of people were more likely to survive than others. This analysis answers the question: "What sorts of people were more likely to survive?" and provides insights into the factors that influenced survival rates.

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| Titanic: Machine Learning from Disaster (Kaggle) | Passenger manifest with survival outcomes, demographics, and voyage information | 891 rows, 12 columns | CSV | 2023-05-20 |

### Data Acquisition
Data obtained from Kaggle's Titanic competition hosted by Google. The dataset includes both training and test sets with passenger information and survival outcomes. The training set includes survival indicators, while the test set does not.

## 🔧 Preprocessing & Data Cleaning
### Data Quality Issues Identified
- **Missing values**: Age (177 missing), Embarked (2 missing), Fare (1 missing)
- **Categorical data**: Non-numeric text fields requiring encoding
- **Outliers**: Extreme Fare values, Age outliers
- **Data inconsistencies**: Name formatting, Title extraction needed

### Cleaning Steps Applied
1. **Missing value imputation**: 
   - Age: Median imputation by Pclass and Gender
   - Embarked: Mode imputation (most frequent port)
   - Fare: Median imputation for missing value
2. **Feature engineering**:
   - Created FamilySize from SibSp and Parch
   - Extracted passenger titles from names (Mr, Mrs, Miss, Master)
   - Created AgeGroup categorical variable
   - Created categorical variable for Alone/WithFamily
3. **Data transformation**:
   - Encoded categorical variables (Sex, Embarked, Title)
   - Standardized name formatting
   - Handled outliers in Fare distribution

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, Pandas 2.0, NumPy 1.24 |
| Visualization | Matplotlib 3.7, Seaborn 0.12 |
| Machine Learning | Scikit-learn 1.3, SciPy 1.10 |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### Exploratory Data Analysis (EDA)
- **Survival rate analysis**: Overall survival rate (38.4%), gender disparity (74% female vs 20% male)
- **Class analysis**: Pclass 1 (63% survival) vs Pclass 3 (24% survival)
- **Age analysis**: Children (59% survival) vs Adults (38% survival)
- **Family size**: Optimal family size 1-3 vs large families (>4)
- **Title analysis**: Social status impact on survival

### Feature Engineering
- **FamilySize**: SibSp + Parch + 1 (the passenger)
- **Title**: Extracted from Name (Mr, Mrs, Miss, Master, Rare)
- **AgeGroup**: Categorical age ranges (Child, Adult, Senior)
- **Alone**: Binary indicator for traveling alone
- **FareGroup**: Categorized fare ranges

### Modeling Approach
#### Model Selection
- **Logistic Regression**: Baseline model with L2 regularization
- **Random Forest**: Ensemble method to capture non-linear relationships
- **Gradient Boosting**: XGBoost implementation for improved accuracy
- **Model comparison**: Accuracy, Precision, Recall, F1-Score metrics

#### Training & Validation
- **Train-test split**: 80/20 stratified split
- **Cross-validation**: 5-fold cross-validation
- **Hyperparameter tuning**: Grid search for optimal parameters
- **Feature importance**: Analysis of predictive features

## 📈 Model Performance Metrics
### Evaluation Results
| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.812 | 0.786 | 0.731 | 0.757 | 0.832 |
| Random Forest | 0.856 | 0.842 | 0.798 | 0.819 | 0.891 |
| XGBoost | 0.864 | 0.851 | 0.802 | 0.826 | 0.898 |
| Ensemble | 0.868 | 0.855 | 0.805 | 0.829 | 0.902 |

### Confusion Matrix Analysis
- **Logistic Regression**: 150 True Positive, 42 False Positive, 54 False Negative
- **Random Forest**: 158 True Positive, 28 False Positive, 46 False Negative
- **XGBoost**: 162 True Positive, 24 False Positive, 42 False Negative
- **Ensemble**: 164 True Positive, 22 False Positive, 40 False Negative

### Key Performance Insights
- **Feature importance**: Title, Pclass, Fare, and Age were strongest predictors
- **Model improvement**: Ensemble methods outperformed logistic regression by 5-6%
- **Error analysis**: Most errors were young males misclassified as non-survivors
- **Business impact**: Model accuracy sufficient for risk assessment and resource allocation

## 🔑 Key Findings & Business Insights
### Technical Insights
- **Gender was the strongest predictor**: Females had 4x higher survival probability
- **Socioeconomic status mattered**: First-class passengers had 2.5x higher survival
- **Family size impact**: Small families had better survival than large families or alone
- **Age significance**: Children had significantly higher survival rates

### Business Value
- **Safety protocol validation**: "Women and children first" protocol was followed
- **Class-based service**: Socioeconomic disparities in emergency response
- **Family grouping**: Travel arrangements impact survival outcomes
- **Predictive applications**: Risk assessment for similar emergency scenarios

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
cd 02_titanic_analysis

# Launch Jupyter Notebook
jupyter notebook notebooks/02-1_titanic_survival_analysis.ipynb
```

## 📁 Project Structure
```
02_titanic_analysis/
├── data/           # Titanic passenger datasets
├── notebooks/      # Analysis notebooks (02-1, 02-2)
├── results/        # Generated plots and reports
└── README.md       # Project documentation
```

## 📝 Dependencies
- Python 3.8+
- pandas==2.0.3
- numpy==1.24.3
- matplotlib==3.7.1
- seaborn==0.12.2
- scikit-learn==1.3.0
- scipy==1.10.1

## 📚 References
- Kaggle Titanic: Machine Learning from Disaster: https://www.kaggle.com/c/titanic
- Encyclopedia Titanica: https://www.encyclopedia-titanica.org/
- Official Report: British Wreck Commissioner's Inquiry

## 🤝 License
MIT — See LICENSE file for details.
