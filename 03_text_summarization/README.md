# Extractive Text Summarization

## 📌 Overview
Frequency-based NLP pipeline that automatically generates summaries from domain-specific articles. Uses NLTK for sentence tokenisation, word frequency scoring, and threshold-based sentence selection to produce concise summaries.

## 🎯 Problem Statement
In the age of information overload, manual reading and summarization of large documents is time-consuming. Automated text summarization provides a solution by using algorithms to identify and retain key information while discarding redundancy. This project aims to build an extractive summarizer that can condense articles into their main points.

## 📂 Data Sources
| Data Source | Description | Size | Format | Access Date |
|-------------|-------------|------|--------|-------------|
| Sample News Articles | Collection of domain-specific articles for summarization | 10-15 articles | Text files | 2023-06-01 |

### Data Acquisition
Sample articles were manually collected from various news sources covering technology, business, and general interest topics. The articles range from 500-2000 words and represent diverse writing styles and content domains.

## 🔧 Preprocessing & Data Cleaning
### Data Quality Issues Identified
- **Text formatting**: Inconsistent paragraph breaks, extra whitespace
- **Special characters**: HTML entities, punctuation variations
- **Stop words**: Common words that add little semantic value
- **Case sensitivity**: Mixed uppercase/lowercase text
- **Sentence boundaries**: Abbreviations causing incorrect tokenization

### Cleaning Steps Applied
1. **Text normalization**:
   - Converted all text to lowercase
   - Removed extra whitespace and line breaks
   - Cleaned HTML entities and special characters
2. **Sentence tokenization**:
   - Split text into individual sentences using NLTK's sentence tokenizer
   - Handled abbreviations and edge cases
3. **Word tokenization**:
   - Split sentences into individual words
   - Removed punctuation and special characters
4. **Stopword removal**:
   - Filtered out common English stopwords using NLTK's corpus
   - Custom stopword list for domain-specific terms
5. **Frequency analysis**:
   - Calculated word frequencies across the document
   - Applied weighted scoring for term importance

## 🛠 Tools & Tech Stack
| Category | Tools & Libraries |
|----------|-------------------|
| Core | Python 3.8, NLTK 3.8, NumPy 1.24 |
| Text Processing | NLTK Tokenizers, Regex, Heapq |
| Development | Jupyter Notebook 6.5, Git |

## 📊 Methodology
### Text Preprocessing Pipeline
1. **Text Cleaning**: Removal of special characters, digits, and extra spaces
2. **Tokenization**: Splitting text into sentences and words
3. **Stopword Removal**: Filtering out common words (e.g., "the", "is")
4. **Frequency Calculation**: Counting word occurrences and normalizing

### Frequency Analysis
- **Word Frequency**: Calculating the occurrence of each word to determine its importance
- **Weighted Frequency**: Normalizing frequencies to score words relative to the most frequent word
- **Sentence Scoring**: Summing weighted frequencies of constituent words

### Summary Generation
- **Sentence Selection**: Using heapq to select top N sentences with highest scores
- **Summary Construction**: Concatenating selected sentences to form final summary
- **Length Optimization**: Balancing summary length vs. information retention

## 🔑 Key Concepts
- **Extractive Summarization**: Selecting existing sentences rather than generating new ones (Abstractive)
- **TF-IDF Logic**: Frequency-based scoring where frequent, non-stop words drive meaning
- **Sentence Scoring**: Each sentence's importance based on constituent word frequencies
- **Threshold-based Selection**: Dynamic selection based on score thresholds

## 🚀 How to Run
### Setup
```bash
# Create virtual environment
python -m venv venv && source venv/bin/activate

# Install dependencies with pinned versions
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### Execution
```bash
# Navigate to project
cd 03_text_summarization

# Launch Jupyter Notebook
jupyter notebook notebooks/03_text_summarization.ipynb
```

## 📁 Project Structure
```
03_text_summarization/
├── data/           # Sample articles for summarization
├── notebooks/      # NLP pipeline and summarization notebook
├── results/        # Generated summaries and reports
└── README.md       # Project documentation
```

## 📝 Dependencies
- Python 3.8+
- nltk==3.8.1
- numpy==1.24.3
- heapq (built-in)

## 📚 References
- NLTK Documentation: https://www.nltk.org/
- Text Summarization Techniques: A Review (Alguliev et al.)
- Frequency-based Sentence Scoring Methods

## 🤝 License
MIT — See LICENSE file for details.
