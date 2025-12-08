# Fake News Detection

## 📌 Overview
This project tackles the critical issue of misinformation by building an NLP-based classification model to detect fake news. It explores various feature engineering techniques, including TF-IDF vectors and Part-of-Speech (POS) tagging with SpaCy, to differentiate between real and fake content.

## 🎯 Problem Statement
"Fake news" causes confusion and can manipulate public opinion. Automating the detection of deceptive content is essential for social media and news platforms. This project aims to classify news items as "Real" or "Fake" based on their textual content.

## 🛠 Tools & Tech Stack
- **Python**: Core Language.
- **Scikit-Learn**: For vectorization (`CountVectorizer`, `TfidfVectorizer`), modeling, and evaluation metrics (ROC-AUC, Precision/Recall).
- **SpaCy**: Used for advanced NLP tasks like Part-of-Speech (POS) tagging to generate linguistic features (noun/verb counts).
- **Pandas & NumPy**: Data manipulation.
- **Seaborn**: Confusion matrix and data visualization.

## 📊 Methodology
1. **Data Cleaning**:
   - Handled missing values.
   - Merged "unknown" labels from the training set into the test set to maintain data integrity.
   - Binary Classification Mapping: Grouped labels like 'false', 'barely true', 'half true' into **FAKE (1)**, and 'true', 'mostly true' into **REAL (0)**.
2. **Feature Engineering**:
   - **Text Stats**: Calculated word counts, char counts, and punctuation usage.
   - **Linguistic Features**: Used SpaCy to count Adjectives, Verbs, Nouns, etc., hypothesizing that fake news might use more emotive language (adjectives) than factual news.
   - **Vectorization**: Converted text into numerical vectors using Bag-of-Words and TF-IDF.
3. **Model Selection**:
   - Evaluated models based on Accuracy, Precision, Recall, and ROC-AUC scores.

## 🔑 Key Concepts
- **Feature Richness**: Beyond simple words, the *structure* of the text (pos-tags, punctuation) can be a strong predictor of deception.
- **Binary Classification**: Transforming a multi-class problem (6 labels) into a binary one to simplify and focus the fraud detection task.

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
   jupyter notebook "06_fake_news_detection.ipynb"
   ```
