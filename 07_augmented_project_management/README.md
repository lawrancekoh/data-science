# AI-Augmented Project Management (Capstone)

## 📌 Overview
This project leverages Machine Learning and Natural Language Processing (NLP) to automate the classification of project management tasks. By analyzing task descriptions, the system predicts appropriate labels/categories, helping to streamline project tracking and reduce manual administrative overhead.

## 🎯 Problem Statement
In large-scale infrastructure and engineering projects, thousands of task descriptions are generated. Manually categorizing these tasks for reporting and analytics is time-consuming and prone to human error. This project aims to build an "AI Assistant" that can automatically tag tasks based on their textual description.

## 🛠 Approach
1. **Data Preprocessing**:
   - Tokenization and lemmatization using `Spacy`.
   - removal of stop words and punctuation.
   - Text cleaning (regex for artifacts).
2. **Feature Engineering**:
   - TF-IDF Vectorization to convert text to numerical features.
3. **Modeling**:
   - Tested multiple classifiers: **Logistic Regression**, **Multinomial Naive Bayes**, **Random Forest**, **Gradient Boosting**.
   - Implemented a **Stacking Classifier** to combine the strengths of these models.
4. **Evaluation**:
   - Metrics: Accuracy, F1-Score (Micro/Macro/Weighted).
   - Confusion Matrix analysis.

## 📊 Key Results
- **Baseline Models**: Logistic Regression (~77%), Naive Bayes (~73%).
- **Ensemble Methods**: Random Forest achieved **~82%** accuracy.
- **Final Model**: A Stacking Classifier (combining NB, RF, GB) achieved the highest performance with **84.2% Accuracy** on the test set.

## 📂 Project Structure
```text
├── data/           # Raw dataset (Excel)
├── notebooks/      # Jupyter notebook with full analysis
├── results/        # (Optional) Generated plots and reports
└── README.md       # This documentation
```

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Navigate to notebooks:
   ```bash
   cd notebooks
   jupyter notebook "07_augmented_project_management.ipynb"
   ```
3. Run all cells to reproduce the analysis.

## 📝 Dependencies
- Python 3.8+
- Scikit-learn
- Pandas, Numpy
- Spacy (en_core_web_sm)
- NLTK
