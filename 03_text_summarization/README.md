# Text Summarization

## 📌 Overview
This project demonstrates the application of Natural Language Processing (NLP) techniques to automatically summarize text documents. By calculating word frequencies and sentence scores, the system extracts the most significant sentences to form a coherent summary, enabling users to quickly grasp the core content of larger texts.

## 🎯 Problem Statement
In the age of information overload, manual reading and summarization of large documents is time-consuming. Automated text summarization provides a solution by using algorithms to identify and retain key information while discarding redundancy.

## 🛠 Tools & Tech Stack
- **Python**: Core language.
- **NLTK (Natural Language Toolkit)**: Primary library for NLP tasks such as tokenization and stopword removal.
- **Regular Expressions (re)**: Used for text cleaning and preprocessing.
- **Heapq**: Utilized to identify and extract top-ranked sentences based on scores.

## 📊 Approach
1. **Text Preprocessing**:
   - **Cleaning**: Removal of special characters, digits, and extra spaces.
   - **Tokenization**: Splitting text into individual sentences and words.
   - **Stopword Removal**: Filtering out common words (e.g., "the", "is") that carry little semantic meaning.
2. **Frequency Analysis**:
   - **Word Frequency**: Calculating the occurrence of each word to determine its importance.
   - **Weighted Frequency**: Normalizing frequencies to score words relative to the most frequent word.
3. **Sentence Scoring**:
   - Calculating scores for each sentence by summing the weighted frequencies of its constituent words.
4. **Summary Generation**:
   - Using `heapq` to select the top $N$ sentences with the highest scores.
   - Concatenating selected sentences to form the final summary.

## 🔑 Key Concepts
- **Extractive Summarization**: The method largely focuses on selecting existing sentences rather than generating new ones (Abstractive).
- **TF-IDF Logic**: The underlying logic mirrors Term Frequency concepts where frequent, non-stop words drive meaning.

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. Navigate to the notebooks directory:
   ```bash
   cd notebooks
   ```
3. Open the notebook:
   ```bash
   jupyter notebook "03_text_summarization.ipynb"
   ```
